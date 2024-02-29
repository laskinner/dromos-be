from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

# Create a router
router = DefaultRouter()
# Register the CommentViewSet with the router
router.register("", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]
