from rest_framework import serializers
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)
    # Dynamic fields like x, y, color, and laber are not included
    # as they are not included in model

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
            "comments_count",
        ]
        read_only_fields = ("owner",)

    def validate_caused_by(self, value):
        # Validate that a node cannot cause itself
        if self.instance and self.instance in value:
            raise serializers.ValidationError("A node cannot cause itself.")
        return value

    def create(self, validated_data):
        # Since the dynamic fields are not part of the Node model,
        # they should not be included in validated_data
        return super().create(validated_data)

    def to_representation(self, instance):
        """
        You can override to_representation if you need
        to send dynamic fields back in the response.
        """
        ret = super().to_representation(instance)
        # Add dynamic fields to the response if needed
        ret["x"] = 0.0  # Example dynamic value
        ret["y"] = 0.0
        ret["size"] = 10.0
        ret["color"] = "blue"
        ret["label"] = instance.title  # Use the title as label if needed
        return ret
