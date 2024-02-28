# profiles/views.py
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from dromos_be.permissions import IsOwnerOrReadOnly


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Apply the custom permission

    def get_serializer_context(self):
        context = super(ProfileViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
