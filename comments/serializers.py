from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Comment

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    profile_id = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    owner_username = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Comment
        fields = (
            "id",
            "node",
            "owner_username",
            "content",
            "created_at",
            "updated_at",
            "profile_id",
            "profile_image",
        )
        read_only_fields = ("owner",)

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
