from rest_framework import serializers
from .models import Area


class AreaSerializer(serializers.ModelSerializer):
    subscribers_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Area
        fields = [
            "id",
            "name",
            "content",
            "image",
            "slug",
            "status",
            "is_public",
            "owner",
            "created_at",
            "updated_at",
            "subscribers_count",
        ]
