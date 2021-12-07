"""Balances views."""
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from coin_usage.accounts.models import Balance
from coin_usage.accounts.serializers import BalanceUserCoinSerializer


class BalanceViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Balance viewset."""

    queryset = Balance.objects.all()
    serializer_class = BalanceUserCoinSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        return [IsAuthenticated(), IsAdminUser()]

    def list(self, request):
        """List balances."""
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
