from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
from .models import Node


def generate_random_position():
    return random.uniform(0, 1000)


@receiver(pre_save, sender=Node)
def set_default_positions(sender, instance, **kwargs):
    if instance.x is None:
        instance.x = generate_random_position()
    if instance.y is None:
        instance.y = generate_random_position()
