"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from strawberry.django.views import GraphQLView
from .schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/v1/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    path("api/v1/contents/", include("contents.urls")),
    path("api/v1/tasks/", include("tasks.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/medias/", include("medias.urls")),
    path("api/v1/followings/", include("followings.urls")),
    path("api/v1/lovings/", include("lovings.urls")),
    path("api/v1/followlists/", include("followlists.urls")),
    path("api/v1/users/", include("users.urls")),
    path("graphql", GraphQLView.as_view(schema=schema)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
