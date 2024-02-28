# profiles/serializers.py
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # Set the owner field to read-only
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "name",
            "content",
            "image",
            "created_at",
            "updated_at",
            "is_owner",
        ]

    def get_is_owner(self, obj):
        return self.context["request"].user == obj.owner
