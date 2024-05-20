from rest_framework import viewsets
from .models import Edge
from .serializers import EdgeSerializer
from nodes.models import Node  # Ensure Node is imported


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
