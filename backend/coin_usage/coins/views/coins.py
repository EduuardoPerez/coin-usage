"""Coin views."""
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from coin_usage.coins.serializers import CoinModelSerializer


class CoinViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """Coin view set."""

    serializer_class = CoinModelSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        return [IsAuthenticated(), IsAdminUser()]

    def perform_create(self, serializer):
        """Create a coin."""
        serializer.save()
