from rest_framework import serializers

from drf_spectacular.utils import OpenApiResponse


class BadRequestResponse(serializers.Serializer):
    message = serializers.CharField()


NotFoundResponse = OpenApiResponse(
    description='Не найдено',
    response=BadRequestResponse,
)
