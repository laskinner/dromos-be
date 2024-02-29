from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from areas.models import Area


class Node(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="nodes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", default="../ik2vexictnekhozluivi")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="nodes")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    def save(self, *args, **kwargs):
        if not self.slug:  # If no slug has been provided, generate one from the title
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # Assumes a many-to-amy relationship with other nodes
    caused_by = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="causes",  # Outgoing edges: Nodes that this node causes
        blank=True,
    )

    def __str__(self):
        return self.title


from . import signals
