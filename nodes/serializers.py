from rest_framework import serializers
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")

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
            "owner",
        ]
