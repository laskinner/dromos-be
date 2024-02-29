from django.db.models.signals import m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed)
def update_edges(sender, instance, action, pk_set, **kwargs):
    # Moved import here to avoid circular import
    from .models import Node
    from edges.models import Edge

    if sender == Node.caused_by.through:
        if action == "post_add":
            # For each new caused_by relationship, create an edge
            for pk in pk_set:
                Edge.objects.create(source_id=pk, target=instance)
        elif action == "post_remove":
            # Remove corresponding edges for removed caused_by relationships
            Edge.objects.filter(source_id__in=pk_set, target=instance).delete()
