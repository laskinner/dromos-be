# areas/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AreaViewSet

router = DefaultRouter()

router.register(r"", AreaViewSet, basename="areas")

urlpatterns = [
    path("", include(router.urls)),
]
