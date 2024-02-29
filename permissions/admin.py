from django.contrib import admin
from .models import UserAreaAccess


@admin.register(UserAreaAccess)
class UserAreaAccessAdmin(admin.ModelAdmin):
    list_display = ("user", "area", "granted_by", "granted_at")
    list_filter = ("area", "granted_by")
    search_fields = ("user__username", "area__name")
