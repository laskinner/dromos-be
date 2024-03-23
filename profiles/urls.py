from django.urls import path, include
from .views import ProfileViewSet, user_details
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", ProfileViewSet, basename="profile")

urlpatterns = [
    path("user/", user_details, name="user-details"),
    path("", include(router.urls)),
    # Add the test endpoint
]
