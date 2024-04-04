from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from dromos_be.permissions import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Optionally restricts the returned comments to a given node,
        by filtering against a `node` query parameter in the URL.
        """

        # Ensure base implementation is called
        queryset = super().get_queryset()
        node_id = self.request.query_params.get("node")
        if node_id is not None:
            queryset = queryset.filter(node__id=node_id)
        return queryset

    def perform_create(self, serializer):
        # Assuming `owner` is automatically added from the logged-in user
        serializer.save(owner=self.request.user)
