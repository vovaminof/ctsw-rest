from rest_framework import serializers

from resource.models import Resource, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ("category", "name", "link")
