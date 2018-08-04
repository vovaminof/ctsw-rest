from rest_framework import viewsets

from resource.models import Resource, Category
from resource.serializers import ResourceSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(active=True).order_by("order")
    serializer_class = CategorySerializer

    http_method_names = ["get"]


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(category__active=True).order_by("category__order")
    serializer_class = ResourceSerializer

    http_method_names = ["get"]
