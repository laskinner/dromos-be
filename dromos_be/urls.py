from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("profiles.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("areas.urls")),
    path("api/", include("nodes.urls")),
]
