"""Accounts serializers."""
from rest_framework import serializers

from coin_usage.accounts.models import Account


class DepositCoinSerializer(serializers.ModelSerializer):
    """Deposit coin into account serializer."""

    coin = serializers.CharField(max_length=5)
    amount = serializers.FloatField()

    class Meta:
        """Meta class."""

        model = Account
        fields = ("coin", "amount")
