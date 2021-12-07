"""Transactions views."""
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from coin_usage.transactions.models import Transaction
from coin_usage.transactions.serializers import TransactionModelSerializer


class TransactionViewSet(ListModelMixin, GenericViewSet):
    """Transaction viewset."""

    serializer_class = TransactionModelSerializer

    def get_queryset(self):
        """Get queryset."""
        if self.action == "list":
            return Transaction.objects.all()

    def get_permissions(self):
        """Assign permissions."""
        return [AllowAny()]
