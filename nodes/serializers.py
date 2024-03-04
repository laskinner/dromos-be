from rest_framework import serializers
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Node
        fields = "__all__"  # Include 'comments_count' in your fields

    def validate_caused_by(self, value):
        if self.instance in value:
            raise serializers.ValidationError("A node cannot cause itself.")
        return value
