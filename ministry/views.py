from rest_framework import viewsets

from ministry.models import Ministry
from ministry.serializers import MinistrySerializer


class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.filter(active=True)
    serializer_class = MinistrySerializer

    http_method_names = ["get"]
