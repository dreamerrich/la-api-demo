from rest_framework import serializers
from .models import Project

class projectSerializers(serializers.Serializer):
    class Meta:
        model = Project
        fields = "__all__"
