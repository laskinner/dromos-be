from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from edges.views import GraphData

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("profiles.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("areas.urls")),
    path("api/", include("nodes.urls")),
    path("api/graph-data/<str:area_slug>/", GraphData.as_view(), name="graph-data"),
    path("api/", include("comments.urls")),
    path("api/", include("subscriptions.urls")),
]
