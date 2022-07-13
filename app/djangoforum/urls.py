"""djangoforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view


api_urlpattern = [
    # API Views
    path('api/', include('topic.api_urls')),
]

urlpatterns = api_urlpattern + [
    # Views
    path('', include('topic.urls')),
    path('users/', include('user.urls')),

    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),

    # API Documentation
    path('openapi', get_schema_view(
            title="API Django Forum",
            description="Django Forum API Documentation",
            version="1.0.0",
            patterns=api_urlpattern,
        ), name='openapi-schema'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
]
