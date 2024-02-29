from django.contrib import admin
from .models import Area
from permissions.models import UserAreaAccess


# Define the inline admin for UserAreaAccess
class UserAreaAccessInline(admin.TabularInline):
    model = UserAreaAccess
    extra = 1  # Number of extra forms to display


@admin.register(Area)
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
    inlines = [UserAreaAccessInline]  # Include the inline defined above
