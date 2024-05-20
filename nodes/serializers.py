from rest_framework import serializers
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = [
            "id",
            "title",
            "content",
            "image",
            "area",
            "status",
            "x",
            "y",
            "caused_by",
        ]
