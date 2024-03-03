from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserAreaAccess
from subscriptions.models import Subscription


@receiver(post_save, sender=UserAreaAccess)
def auto_subscribe_user_to_area(sender, instance, created, **kwargs):
    if created:
        Subscription.objects.create(user=instance.user, area=instance.area)
