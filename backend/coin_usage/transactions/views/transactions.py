"""Transactions views."""
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from coin_usage.transactions.models import Transaction
from coin_usage.transactions.serializers import TransactionModelSerializer


class TransactionViewSet(ListModelMixin, GenericViewSet):
    """Transaction viewset."""

    def get_serializer_class(self):
        """Return appropriate serializer class."""
        return TransactionModelSerializer

    def get_queryset(self):
        """Get queryset."""
        if self.action == "list":
            return Transaction.objects.all()
        if self.action == "accounts":
            return Transaction.objects.filter(
                Q(account_from=self.request.user.account) | Q(account_to=self.request.user.account)
            )

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action == "accounts":
            return [IsAuthenticated()]
        return [AllowAny()]

    @action(detail=False, methods=["GET"])
    def accounts(self, request, *args, **kwargs):
        """Get the transactions of the account."""
        serializer = self.get_serializer(self.filter_queryset(self.get_queryset()), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
