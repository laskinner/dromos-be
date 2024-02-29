from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        # Custom logic to handle subscription creation
        return super().create(request, *args, **kwargs)
