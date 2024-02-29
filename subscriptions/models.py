from django.db import models
from django.contrib.auth.models import User
from areas.models import Area


class Subscription(models.Model):
    user = models.ForeignKey(
        User, related_name="area_subscriptions", on_delete=models.CASCADE
    )
    area = models.ForeignKey(Area, related_name="subscribers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "area")  # Prevents duplicate subscriptions

    def __str__(self):
        return f"{self.user.username} subscribed to {self.area.name}"
