from django.db import models
from django.contrib.auth.models import User
from areas.models import Area


class UserAreaAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="area_access")
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name="access_users"
    )
    granted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="granted_accesses"
    )
    granted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "area")  # Ensures unique access per area per user

    def __str__(self):
        return f"{self.user.username} has access to {self.area.name}"
