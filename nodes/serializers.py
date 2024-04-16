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
        # This will only trigger in cases of update where self.instance is defined
        if self.instance:
            if self.instance.id in [node.id for node in value]:
                raise serializers.ValidationError("A node cannot cause itself.")
        return value

    def create(self, validated_data):
        caused_by_ids = validated_data.pop("caused_by", [])
        node = Node.objects.create(**validated_data)  # Create the node first

        # Create edges for each cause ID provided
        for cause_id in caused_by_ids:
            cause_node = Node.objects.get(
                id=cause_id
            )  # Get the node instance for each cause_id
            Edge.objects.create(source=cause_node, target=node)
            print("Creating edge from", cause_node.id, "to", node.id)

        return node

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update(
            {
                "x": 0.0,
                "y": 0.0,
                "size": 10.0,
                "color": "blue",
                "label": instance.title,
                "caused_by": [node.id for node in instance.caused_by.all()],
            }
        )
        return representation
