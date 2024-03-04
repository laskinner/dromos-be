from django.db.models import Count
from rest_framework import viewsets
from .models import Node
from .serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    serializer_class = NodeSerializer

    def get_queryset(self):
        """
        Annotate the queryset with a count of comments for each node.
        """
        return Node.objects.annotate(comments_count=Count("comments", distinct=True))
