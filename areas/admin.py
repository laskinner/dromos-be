from django.contrib import admin
from .models import Area


class AreaAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "status",
        "created_at",
        "updated_at",
    )  # Fields to display in the admin list view
    list_filter = (
        "status",
        "created_at",
        "updated_at",
    )  # Fields to filter by in the admin list view
    search_fields = ("name", "content")  # Fields to search in the admin list view
    prepopulated_fields = {
        "slug": ("name",)
    }  # Automatically populate the slug field from the name field


admin.site.register(Area, AreaAdmin)
