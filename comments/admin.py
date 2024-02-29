from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("owner", "node", "created_at", "content")
    list_filter = ("created_at", "owner")
    search_fields = ("content",)
