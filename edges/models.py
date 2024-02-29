from django.db import models
from nodes.models import Node


class Edge(models.Model):
    source = models.ForeignKey(
        Node, related_name="outgoing_edges", on_delete=models.CASCADE
    )
    target = models.ForeignKey(
        Node, related_name="incoming_edges", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.source.title} causes {self.target.title}"
