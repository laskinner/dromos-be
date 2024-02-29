from django.db import models
from django.conf import settings
from nodes.models import Node


class Comment(models.Model):
    node = models.ForeignKey(Node, related_name="comments", on_delete=models.CASCADE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="node_comments", on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.owner} on {self.node}"
