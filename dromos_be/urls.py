from django.contrib import admin
from django.urls import include, path
from edges.views import GraphData
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import root_route, logout_route
from django.http import JsonResponse


def root_test_view(request):
    return JsonResponse({"message": "Root test endpoint is working"})


urlpatterns = [
    path("", root_route),
    path("admin/", admin.site.urls),
    path("api/profiles/", include("profiles.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/areas/", include("areas.urls")),
    path("api/nodes/", include("nodes.urls")),
    path("api/graph-data/<str:area_slug>/", GraphData.as_view(), name="graph-data"),
    path("api/comments/", include("comments.urls")),
    path("api/root-test/", root_test_view, name="root-test"),
    path("api/subscriptions/", include("subscriptions.urls")),
    path("api/permissions/", include("permissions.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Custom logout before the default dj-rest-auth logout to ensure it's used
    path("dj-rest-auth/logout/", logout_route, name="custom_logout"),
    # dj-rest-auth URLs for authentication
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    # dj-rest-auth registration URLs
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
]
