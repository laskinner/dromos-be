from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Area(models.Model):
    STATUS_CHOICES = (
        ("public", "Public"),
        ("private", "Private"),
        ("archived", "Archived"),
    )

    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="owned_areas"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="areas_images/", blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="public")
    contributors = models.ManyToManyField(
        User, related_name="contributing_areas", blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Area, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
