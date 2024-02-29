from django.urls import path
from .views import GraphData

urlpatterns = [
    path("graph-data/<str:area_slug>/", GraphData.as_view(), name="graph-data"),
]
