from django.db.models import Count
from rest_framework import viewsets, filters
from .models import Node
from .serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    serializer_class = NodeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "owner__username"]

    def get_queryset(self):
        """
        Annotate the queryset with a count of comments for each node and enables search.
        """
        return Node.objects.annotate(comments_count=Count("comments", distinct=True))
