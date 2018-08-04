from rest_framework import viewsets

from project.models import Project
from project.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(active=True)
    serializer_class = ProjectSerializer

    http_method_names = ["get"]
