from rest_framework import serializers

from about.models import About


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ("id", "name", "content", "summary")
