from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import UserAreaAccess
from .serializers import UserAreaAccessSerializer


class UserAreaAccessViewSet(viewsets.ModelViewSet):
    queryset = UserAreaAccess.objects.all()
    serializer_class = UserAreaAccessSerializer
    permission_classes = [IsAuthenticated]  # Example permission class

    def perform_create(self, serializer):
        serializer.save(granted_by=self.request.user)
