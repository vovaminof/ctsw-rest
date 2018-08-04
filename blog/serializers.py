from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from taggit.models import Tag

from blog.models import Author, Post


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ("id", "creation_time", "author", "title", "text", "image", "tags")


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("name",)


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "name", "about", "image")
