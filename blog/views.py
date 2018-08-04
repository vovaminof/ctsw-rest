from rest_framework import viewsets
from taggit.models import Tag

from blog.models import Post, Author
from blog.serializers import PostSerializer, TagSerializer, AuthorSerializer


class PostViewSet(viewsets.ModelViewSet):
    # TODO:
    # 1. Implement pagination
    # 2. Return author info and less text on post/ query

    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        queryset = self.queryset
        tags = self.request.query_params.get("tags")
        if tags:
            queryset = queryset.filter(tags__name__in=tags.split(","))

        return queryset


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names = ["get"]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ["get"]