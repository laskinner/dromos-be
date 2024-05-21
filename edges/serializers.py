from rest_framework import serializers
from .models import Edge
from nodes.models import Node


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = ("id", "source", "target")  # Adjust fields as needed

    def validate(self, data):
        """
        Check that the source and target nodes exist and are not the same.
        """
        if data["source"] == data["target"]:
            raise serializers.ValidationError(
                "Source and target cannot be the same node."
            )
        return data
