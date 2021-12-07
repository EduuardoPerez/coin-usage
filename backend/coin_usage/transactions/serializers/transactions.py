"""Transactions serializers."""
from rest_framework.serializers import CharField, ModelSerializer

from coin_usage.transactions.models import Transaction


class TransactionModelSerializer(ModelSerializer):
    """Transaction model serializer."""

    account_from = CharField(source="account_from.address")
    account_to = CharField(source="account_to.address")
    coin = CharField(source="coin.ticker_symbol")

    class Meta:
        """Meta class."""

        model = Transaction
        fields = ("created", "account_from", "account_to", "coin", "amount")
