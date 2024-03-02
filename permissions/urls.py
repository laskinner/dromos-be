from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserAreaAccessViewSet

router = DefaultRouter()
router.register(r"", UserAreaAccessViewSet, basename="userareaaccess")

urlpatterns = [
    path("", include(router.urls)),
]
