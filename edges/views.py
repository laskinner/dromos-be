from rest_framework.views import APIView
from rest_framework.response import Response
from nodes.models import Node
from edges.models import Edge
from nodes.serializers import NodeSerializer
from edges.serializers import EdgeSerializer


class GraphData(APIView):
    def get(self, request, area_slug, format=None):
        # Fetch nodes and edges related to the area to be displayed
        nodes = Node.objects.filter(area__slug=area_slug)
        edges = Edge.objects.filter(source__in=nodes, target__in=nodes)

        node_serializer = NodeSerializer(nodes, many=True)
        edge_serializer = EdgeSerializer(edges, many=True)

        graph_data = {
            "nodes": node_serializer.data,
            "edges": edge_serializer.data,
        }
        return Response(graph_data)  # Use Response instead of JsonResponse
