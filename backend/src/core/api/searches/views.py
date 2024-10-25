from rest_framework import (
    serializers,
    status,
)
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from drf_spectacular.utils import (
    extend_schema,
    inline_serializer,
)

from core.api.common.openapi_serializers import (
    BadRequestResponse,
    NotFoundResponse,
)
from core.api.controllers import catch_use_case_errors_as_view
from core.domain.searches.usecases.create_search import CreateSearchUseCase
from core.infra.searches.constants import SearchFilterOperatorChoices
from core.infra.searches.repositories.search import search_read_repository


class SearchViewSet(ViewSet):

    class CreateSearchSerializer(serializers.Serializer):
        search_id = serializers.UUIDField(read_only=True)

        text = serializers.CharField(
            write_only=True,
            allow_null=True,
            allow_blank=True,
            required=False,
        )
        file_mask = serializers.CharField(
            write_only=True,
            allow_null=True,
            allow_blank=True,
            required=False,
        )

        size = inline_serializer(
            name='SearchSizeSerializer',
            fields={
                'value': serializers.IntegerField(),
                'operator': serializers.ChoiceField(
                    choices=SearchFilterOperatorChoices.choices,
                ),
            },
            write_only=True,
            allow_null=True,
            required=False,
        )

        creation_time = inline_serializer(
            name='SearchCreationTimeSerializer',
            fields={
                'value': serializers.DateTimeField(),
                'operator': serializers.ChoiceField(
                    choices=SearchFilterOperatorChoices.choices,
                ),
            },
            write_only=True,
            allow_null=True,
            required=False,
        )

    class SearchSerializer(serializers.Serializer):
        search_id = serializers.UUIDField()
        finished = serializers.BooleanField()
        results = serializers.ListField(child=serializers.CharField())
        search_filter = inline_serializer(
            name='SearchListFilterSerializer',
            fields={
                'text': serializers.CharField(allow_blank=True),
                'file_mask': serializers.CharField(allow_blank=True),
                'size': serializers.IntegerField(allow_null=True),
                'size_operator': serializers.CharField(allow_blank=True),
                'creation_date': serializers.DateTimeField(allow_null=True),
                'creation_date_operator': serializers.CharField(allow_blank=True),
            },
        )

    class SearchListSerializer(serializers.Serializer):
        search_id = serializers.UUIDField()
        finished = serializers.BooleanField()
        created_at = serializers.DateTimeField()
        search_filter = inline_serializer(
            name='SearchListFilterSerializer',
            fields={
                'text': serializers.CharField(allow_blank=True),
                'file_mask': serializers.CharField(allow_blank=True),
                'size': serializers.IntegerField(allow_null=True),
                'size_operator': serializers.CharField(allow_blank=True),
                'creation_date': serializers.DateTimeField(allow_null=True),
                'creation_date_operator': serializers.CharField(allow_blank=True),
            },
        )

    @extend_schema(
        operation_id='createSearch',
        description='Метод по созданию поискового запроса',
        request=CreateSearchSerializer,
        responses={
            status.HTTP_201_CREATED: CreateSearchSerializer,
            status.HTTP_400_BAD_REQUEST: BadRequestResponse,
        },
    )
    @catch_use_case_errors_as_view
    def create(self, request, *args, **kwargs):
        in_serializer = self.CreateSearchSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)

        use_case = CreateSearchUseCase(
            text=in_serializer.validated_data.get('text', ''),
            file_mask=in_serializer.validated_data.get('file_mask', ''),
            default_size=in_serializer.validated_data.get('size'),
            default_creation_time=in_serializer.validated_data.get('creation_time'),
        )

        search = use_case.execute()

        out_serializer = self.CreateSearchSerializer(instance=search)

        return Response(out_serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        operation_id='getSearchDetail',
        description='Метод по получению поискового запроса',
        responses={
            status.HTTP_200_OK: SearchSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundResponse,
        },
    )
    def retrieve(self, request, search_id, *args, **kwargs):
        search = get_object_or_404(search_read_repository.get_many().with_search_filter(), search_id=search_id)

        out_serializer = self.SearchSerializer(instance=search)

        return Response(out_serializer.data)

    @extend_schema(
        operation_id='getSearchList',
        description='Метод по получению списка поисковых запросов',
        responses={
            status.HTTP_200_OK: SearchListSerializer,
            status.HTTP_404_NOT_FOUND: NotFoundResponse,
        },
    )
    def list(self, request, *args, **kwargs):
        searches = search_read_repository.get_many().with_search_filter().order_by('-created_at')

        out_serializer = self.SearchListSerializer(searches, many=True)

        return Response(out_serializer.data)
