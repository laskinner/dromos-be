from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from edges.views import GraphData

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/profiles/", include("profiles.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/areas/", include("areas.urls")),
    path("api/nodes/", include("nodes.urls")),
    path("api/graph-data/<str:area_slug>/", GraphData.as_view(), name="graph-data"),
    path("api/comments/", include("comments.urls")),
    path("api/subscriptions/", include("subscriptions.urls")),  # Adjusted
    path("api/permissions/", include("permissions.urls")),  # Adjusted
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
