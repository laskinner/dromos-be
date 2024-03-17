from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, user_details

router = DefaultRouter()
router.register(r"", ProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls)),
    path("user/", user_details, name="user-details"),
]
