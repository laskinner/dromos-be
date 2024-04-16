from rest_framework import serializers
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)
    x = serializers.FloatField(default=0.0)  # Example fixed position
    y = serializers.FloatField(default=0.0)
    size = serializers.FloatField(default=10.0)  # Default size
    color = serializers.CharField(default="blue")  # Default color
    label = serializers.CharField(
        source="title", required=False, allow_blank=True
    )  # Use the title as label

    class Meta:
        model = Node
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "image",
            "area",
            "status",
            "created_at",
            "updated_at",
            "owner",
            "caused_by",
            "comments_count",  # Include any additional fields here
            "x",
            "y",
            "size",
            "color",
            "label",  # Visualization-specific fields
        ]
        read_only_fields = ("owner",)

    def validate_caused_by(self, value):
        # Validate that a node cannot cause itself
        if self.instance and self.instance in value:
            raise serializers.ValidationError("A node cannot cause itself.")
        return value

    def validate(self, data):
        data["label"] = data.get("label", data.get("title"))
        return data
