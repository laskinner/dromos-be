# profiles/views.py
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from dromos_be.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Apply the custom permission

    def get_serializer_context(self):
        context = super(ProfileViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_details(request):
    # Access the user from the request
    user = request.user
    # Return the user details you need
    return Response(
        {
            "username": user.username,
            "email": user.email,
            # Include other details from the user model or related models as needed
        }
    )
