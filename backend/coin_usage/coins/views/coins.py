"""Coin views."""
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from coin_usage.coins.models import Coin
from coin_usage.coins.serializers import CoinModelSerializer


class CoinViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    """Coin view set."""

    serializer_class = CoinModelSerializer

    def get_queryset(self):
        """Get queryset."""
        return Coin.objects.all()

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action == "create":
            return [IsAuthenticated(), IsAdminUser()]
        if self.action == "list":
            return [AllowAny()]

    def perform_create(self, serializer):
        """Create a coin."""
        serializer.save()
