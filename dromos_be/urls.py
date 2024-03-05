from django.contrib import admin
from django.urls import path, include
from edges.views import GraphData
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/profiles/", include("profiles.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/areas/", include("areas.urls")),
    path("api/nodes/", include("nodes.urls")),
    path("api/graph-data/<str:area_slug>/", GraphData.as_view(), name="graph-data"),
    path("api/comments/", include("comments.urls")),
    path("api/subscriptions/", include("subscriptions.urls")),
    path("api/permissions/", include("permissions.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
