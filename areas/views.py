from django.db.models import Count
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

        # Optionally, override other methods as needed to implement custom logic,
        # such as create() for handling area creation with specific permission checks.
