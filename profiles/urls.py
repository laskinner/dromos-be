from django.urls import path, include
from django.http import JsonResponse
from .views import ProfileViewSet, user_details
from rest_framework.routers import DefaultRouter


# Define the test_view function
def test_view(request):
    return JsonResponse({"message": "Test endpoint is working"})


router = DefaultRouter()
router.register(r"", ProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls)),
    path("user/", user_details, name="user-details"),
    # Add the test endpoint
    path("test/", test_view, name="test-view"),
]
