from rest_framework import serializers
from .models import Node, Edge


class NodeSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(read_only=True)

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
        if self.instance and self.instance.id in [node.id for node in value]:
            raise serializers.ValidationError("A node cannot cause itself.")
        return value

    def create(self, validated_data):
        caused_by_ids = validated_data.pop("caused_by", [])
        node = Node.objects.create(**validated_data)  # Create the node first
        # Create edges for each cause ID provided
        for cause_id in caused_by_ids:
            Edge.objects.create(source_id=cause_id, target=node)
        return node

    def to_representation(self, instance):
        """
        Modify to_representation to include dynamic fields and format caused_by properly.
        """
        representation = super().to_representation(instance)
        # Dynamically adds attributes which are not included in model
        representation["x"] = 0.0
        representation["y"] = 0.0
        representation["size"] = 10.0
        representation["color"] = "blue"
        representation["label"] = instance.title  # Use title as label
        # Format caused_by to show IDs or details
        representation["caused_by"] = [node.id for node in instance.caused_by.all()]
        return representation
