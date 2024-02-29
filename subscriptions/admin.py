from django.contrib import admin
from .models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "area", "created_at")
    list_filter = ("user", "area")
    search_fields = ("user__username", "area__name")
