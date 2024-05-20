from django.db.models import Count
from rest_framework import viewsets, filters, serializers
from .models import Node
from .serializers import NodeSerializer
from django.db import transaction


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "owner__username"]

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .annotate(comments_count=Count("comments", distinct=True))
        )
        area_id = self.kwargs.get("area_id")
        if area_id:
            queryset = queryset.filter(area_id=area_id)
        return queryset

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError(
                "User must be authenticated to create a node."
            )
        with transaction.atomic():
            serializer.save(owner=self.request.user)
