from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NodeViewSet

router = DefaultRouter()

router.register(r"", NodeViewSet, basename="node")

urlpatterns = [
    path("", include(router.urls)),
]
