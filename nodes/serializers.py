from rest_framework import serializers
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Node
        fields = "__all__"

    def validate_caused_by(self, value):
        # Validate that a node cannot cause itself
        if self.instance and self.instance in value:
            raise serializers.ValidationError("A node cannot cause itself.")
        return value
