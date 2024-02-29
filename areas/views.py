from rest_framework import viewsets
from .models import Area
from .serializers import AreaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    # If custom permissions should be implemented, add them here. Uncomment below and modify as needed
    # permission_classes = [IsOwnerOrReadOnly]
