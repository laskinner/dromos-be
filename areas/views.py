from django.db.models import Count
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Area
from .serializers import AreaSerializer
from nodes.models import Node
from edges.models import Edge
from nodes.serializers import NodeSerializer
from edges.serializers import EdgeSerializer


class AreaViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing area instances.
    """

    serializer_class = AreaSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]  # Example permission class

    def get_queryset(self):
        """
        Optionally restricts the returned areas to those accessible
        to the current user by filtering against `UserAreaAccess` model.
        """
        user = self.request.user

        if not user.is_authenticated:
            # If the user is not authenticated, return public areas annotated with subscriber count
            return Area.objects.filter(is_public=True).annotate(
                subscribers_count=Count("subscribers", distinct=True)
            )
        else:
            # Construct a queryset of areas accessible to the authenticated user
            accessible_areas = (
                Area.objects.filter(is_public=True)
                | Area.objects.filter(owner=user)
                | Area.objects.filter(access_users__user=user)
            ).annotate(subscribers_count=Count("subscribers", distinct=True))

            return accessible_areas.distinct()


class GraphData(APIView):
    def get(self, request, area_id, format=None):
        nodes = Node.objects.filter(area_id=area_id)
        edges = Edge.objects.filter(source__area_id=area_id)

        node_serializer = NodeSerializer(nodes, many=True)
        edge_serializer = EdgeSerializer(edges, many=True)

        graph_data = {
            "nodes": node_serializer.data,
            "edges": edge_serializer.data,
        }
        return Response(graph_data)  # Use Response instead of JsonResponse
