from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Edge


class AreaFilter(admin.SimpleListFilter):
    title = _("area")
    parameter_name = "area"

    def lookups(self, request, model_admin):
        from areas.models import Area  # Importing here to prevent unused import warning

        areas = Area.objects.all()
        return [(area.id, area.name) for area in areas]

    def queryset(self, request, queryset):
        if self.value():
            # Filters by the ID of the area
            return queryset.filter(source__area__id__exact=self.value())
        return queryset


@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ("id", "source", "target")
    list_filter = (AreaFilter,)
    readonly_fields = (
        "source",
        "target",
    )
