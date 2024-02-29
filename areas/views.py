from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Area
from .serializers import AreaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing area instances.
    """

    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Example permission class

    def get_queryset(self):
        """
        Optionally restricts the returned areas to those accessible to the current user,
        by filtering against a `UserAreaAccess` model.
        """
        queryset = Area.objects.all()
        user = self.request.user

        # If the user is not authenticated, return public areas
        if not user.is_authenticated:
            return queryset.filter(is_public=True)

        # If the user is authenticated, filter areas by public, ownership, or explicit access
        accessible_areas = (
            queryset.filter(is_public=True)
            | queryset.filter(owner=user)
            | queryset.filter(access_users__user=user)
        )

        return (
            accessible_areas.distinct()
        )  # Use distinct() to avoid duplicate areas in the result

    # Optionally, override other methods as needed to implement custom logic,
    # such as create() for handling area creation with specific permission checks.
