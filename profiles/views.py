from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from dromos_be.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Apply custom permission

    def get_serializer_context(self):
        context = super(ProfileViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    profile = Profile.objects.get(
        owner=user
    )  # Get the profile associated with this user

    # Construct the response with details from both the User and Profile models
    return Response(
        {
            "username": user.username,  # This still uses the User model's username
            "email": user.email,  # Email from the User model
            "name": profile.name,  # Name from the Profile model
            # Include other details from the Profile model as needed
            "content": profile.content,
            "image": request.build_absolute_uri(profile.image.url)
            if profile.image
            else None,
        }
    )


@login_required
def current_user_profile(request):
    user = request.user
    return JsonResponse(
        {
            "username": user.username,
            "email": user.email,
        }
    )
