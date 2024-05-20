from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EdgeViewSet

router = DefaultRouter()
router.register(r"", EdgeViewSet, basename="edge")

urlpatterns = [
    path("", include(router.urls)),
]
