"""Transactions serializers."""
from rest_framework.serializers import ModelSerializer

from coin_usage.transactions.models import Transaction


class TransactionModelSerializer(ModelSerializer):
    """Transaction model serializer."""

    class Meta:
        """Meta class."""

        model = Transaction
        fields = ("created", "account_from", "account_to", "coin", "amount")
