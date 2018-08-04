from rest_framework import viewsets

from about.models import About
from about.serializers import AboutSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.filter(active=True)
    serializer_class = AboutSerializer

    http_method_names = ["get"]
