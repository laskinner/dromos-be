from rest_framework import serializers
from .models import Comment
from django.conf import settings


# Base Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    profile_id = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            "id",
            "node",
            "owner",
            "content",
            "created_at",
            "updated_at",
            "profile_id",
            "profile_image",
        )

    def get_profile_id(self, obj):
        return obj.owner.profile.id

    def get_profile_image(self, obj):
        request = self.context.get("request")
        profile_image_url = obj.owner.profile.image.url
        return (
            request.build_absolute_uri(profile_image_url)
            if request
            else profile_image_url
        )


# Detailed Comment Serializer that locks a comment to a specific node
class CommentDetailSerializer(CommentSerializer):
    node = serializers.ReadOnlyField(source="node.id")

    class Meta(CommentSerializer.Meta):
        fields = CommentSerializer.Meta.fields + ("node",)
