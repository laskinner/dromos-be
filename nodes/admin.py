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
    )  # Fields to display in the admin list view
    list_filter = (
        "status",
        "created_at",
        "updated_at",
        "area",
        "owner",
    )  # Fields to filter by in the admin list view
    search_fields = (
        "title",
        "content",
        "owner__username",
        "area__name",
    )  # Fields to search in the admin list view
    prepopulated_fields = {
        "slug": ("title",)
    }  # Automatically populate the slug field from the title field

    # Filter_horizontal to make managing node relationships easier in the admin interface.
    filter_horizontal = ("caused_by",)


admin.site.register(Node, NodeAdmin)
