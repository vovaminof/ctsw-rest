from rest_framework import serializers

from ministry.models import Ministry


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ("id", "name", "content", "image")
