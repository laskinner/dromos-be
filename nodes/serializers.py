from rest_framework import serializers
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = "__all__"

    def validate_caused_by(self, value):
        if self.instance in value:
            raise serializers.ValidationError("A node cannot cause itself.")
        return value
