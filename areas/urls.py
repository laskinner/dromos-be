from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AreaViewSet, GraphData

router = DefaultRouter()
router.register(r"", AreaViewSet, basename="areas")

urlpatterns = [
    path("", include(router.urls)),
    path("graph-data/<int:area_id>/", GraphData.as_view(), name="graph-data"),
]
