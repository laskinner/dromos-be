from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from dromos_be.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Apply custom permission

    def get_serializer_context(self):
        context = super(ProfileViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_details(request):
    user = request.user
    profile = get_object_or_404(Profile, owner=user)
    serializer = ProfileSerializer(profile, context={"request": request})
    return Response(serializer.data)


@login_required
def current_user_profile(request):
    user = request.user
    return JsonResponse(
        {
            "username": user.username,
            "email": user.email,
        }
    )
