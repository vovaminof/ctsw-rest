"""savior URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from ministry.urls import routes as ministry_routes
from project.urls import routes as project_routes
from about.urls import routes as about_routes
from resource.urls import routes as resource_routes
from blog.urls import routes as blog_routes

router = routers.DefaultRouter()
all_routes = (ministry_routes, project_routes, about_routes, resource_routes, blog_routes)

for routes in all_routes:
    for route in routes:
        router.register(*route)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
