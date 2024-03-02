from rest_framework import serializers
from .models import UserAreaAccess


class UserAreaAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAreaAccess
        fields = ["id", "user", "area", "granted_by", "granted_at"]
        read_only_fields = ["granted_by", "granted_at"]
