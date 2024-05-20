from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
import random
from .models import Node
from edges.models import Edge


def generate_random_position():
    return random.uniform(0, 1000)


@receiver(pre_save, sender=Node)
def set_default_positions(sender, instance, **kwargs):
    if instance.x is None:
        instance.x = generate_random_position()
    if instance.y is None:
        instance.y = generate_random_position()


@receiver(m2m_changed, sender=Node.caused_by.through)
def update_edges(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for pk in pk_set:
            Edge.objects.create(source_id=pk, target=instance)
    elif action == "post_remove":
        Edge.objects.filter(source_id__in=pk_set, target=instance).delete()
