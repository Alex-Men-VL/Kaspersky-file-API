from django.urls import path

from .views import SearchViewSet


app_name = 'searches'

urlpatterns = [
    path('', SearchViewSet.as_view({'post': 'create', 'get': 'list'}), name='search-list'),
    path('<str:search_id>/', SearchViewSet.as_view({'get': 'retrieve'}), name='search-detail'),
]
