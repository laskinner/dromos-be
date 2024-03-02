from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

# Create a router
router = DefaultRouter()

router.register("", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]
