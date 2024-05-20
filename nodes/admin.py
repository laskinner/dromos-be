from django.contrib import admin
from .models import Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "status", "created_at", "updated_at"]
    search_fields = ["title", "content"]
