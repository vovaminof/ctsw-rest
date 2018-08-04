from blog.views import PostViewSet, TagViewSet, AuthorViewSet

routes = (
    (r"post", PostViewSet),
    (r"tag", TagViewSet),
    (r"author", AuthorViewSet)
)
