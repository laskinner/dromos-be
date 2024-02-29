from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AreaViewSet

# Create router and register viewsets with it.
router = DefaultRouter()
router.register(r"areas", AreaViewSet)

# API URLs determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
