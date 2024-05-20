from django.contrib import admin
from .models import Node


class NodeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "area",
        "status",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "created_at",
        "updated_at",
        "area",
        "owner",
    )
    search_fields = (
        "title",
        "content",
        "owner__username",
        "area__name",
    )
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Node, NodeAdmin)
