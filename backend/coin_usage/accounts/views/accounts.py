"""Accounts views."""
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from coin_usage.accounts.models import Account
from coin_usage.accounts.serializers import DepositCoinSerializer


class AccountViewSet(viewsets.GenericViewSet):
    """Coin view set."""

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == "deposit":
            return DepositCoinSerializer

    def get_permissions(self):
        """Assign permissions."""
        return [IsAuthenticated()]

    def get_queryset(self):
        """Get queryset."""
        if self.action == "deposit":
            return Account.objects.get(user=self.request.user)

    @action(detail=False, methods=["PATCH"])
    def deposit(self, request, *args, **kwargs):
        """Deposit coin."""
        breakpoint()
        pass
