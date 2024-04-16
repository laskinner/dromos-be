from django.db.models import Count
from rest_framework import viewsets, filters, serializers
from .models import Node
from edges.models import Edge
from edges.serializers import EdgeSerializer
from .serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    """
    A combined ViewSet for handling both individual node operations and listing nodes by area.
    """

    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "owner__username"]

    def get_queryset(self):
        """
        Optionally filters the nodes by area_id if it's provided in the URL.
        """
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
        """Ensure user is authenticated and handle causedBy data for edge creation."""
        if not self.request.user.is_authenticated:
            raise serializers.ValidationError(
                "User must be authenticated to create a node."
            )

        # This will create the node and return the instance
        node = serializer.save(owner=self.request.user)

        # Now handle the 'causedBy' data if it exists
        caused_by_ids = serializer.validated_data.get("caused_by", [])
        for cause_id in caused_by_ids:
            Edge.objects.create(source_id=cause_id, target=node)
            print(f"Edge created from {cause_id} to {node.id}")

        print("Node and associated edges created successfully")


class EdgeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet for listing edges. Assumes that edges are directly related to nodes (i.e., through foreign keys).
    """

    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer

    def get_queryset(self):
        """
        Filters edges to include only those connecting nodes within the specified area.
        """
        area_id = self.kwargs.get("area_id")
        if area_id:
            nodes = Node.objects.filter(area_id=area_id).values_list("id", flat=True)
            queryset = Edge.objects.filter(source_id__in=nodes, target_id__in=nodes)
            return queryset
        return super().get_queryset()
