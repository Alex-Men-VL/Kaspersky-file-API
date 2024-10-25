from django.urls import (
    include,
    path,
)


urlpatterns = [
    path('searches/', include('core.api.searches.urls')),
]
