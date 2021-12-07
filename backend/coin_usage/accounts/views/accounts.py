"""Accounts views."""
from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from coin_usage.accounts.models import Account, Balance
from coin_usage.accounts.serializers import (
    AccountBalancesModelSerializer,
    BalanceCoinSerializer,
    DepositCoinSerializer,
    SendCoinSerializer,
)


class AccountViewSet(viewsets.GenericViewSet):
    """Coin view set."""

    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == "deposit":
            return DepositCoinSerializer
        if self.action == "send":
            return SendCoinSerializer
        if self.action == "coins":
            return BalanceCoinSerializer
        return AccountBalancesModelSerializer

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
        data = AccountBalancesModelSerializer(account).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["PATCH"])
    def send(self, request, *args, **kwargs):
        """Send coin to other user."""
        account = self.request.user.account
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(account, data=request.data, context={"user": request.user}, partial=True)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        data = AccountBalancesModelSerializer(account).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def balances(self, request, *args, **kwargs):
        """Get balances of the user account."""
        account = self.request.user.account
        data = AccountBalancesModelSerializer(account).data
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def coins(self, request, *args, **kwargs):
        """Get balances of a coin of the user account."""
        ticker_symbol = request.query_params.get("coin")
        try:
            balance = self.request.user.account.balances.get(coin__ticker_symbol=ticker_symbol)
        except Balance.DoesNotExist:
            raise ValidationError(_("User does not have a balance for this coin"))
        data = BalanceCoinSerializer(balance).data
        return Response(data, status=status.HTTP_200_OK)
