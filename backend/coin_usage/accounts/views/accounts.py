"""Accounts views."""
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from coin_usage.accounts.models import Account
from coin_usage.accounts.serializers import AccountModelSerializer, DepositCoinSerializer, SendCoinSerializer


class AccountViewSet(viewsets.GenericViewSet):
    """Coin view set."""

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == "deposit":
            return DepositCoinSerializer
        if self.action == "send":
            return SendCoinSerializer
        return AccountModelSerializer

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
        account = self.request.user.account
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(account, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        data = AccountModelSerializer(account).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["PATCH"])
    def send(self, request, *args, **kwargs):
        """Send coin to other user."""
        account = self.request.user.account
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(account, data=request.data, context={"user": request.user}, partial=True)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        data = AccountModelSerializer(account).data
        return Response(data, status=status.HTTP_200_OK)
