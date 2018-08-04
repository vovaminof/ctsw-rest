from resource.views import ResourceViewSet, CategoryViewSet

routes = (
    (r"resource", ResourceViewSet),
    (r"category", CategoryViewSet)
)
