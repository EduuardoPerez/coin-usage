"""Balances serializers."""
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from coin_usage.accounts.models import Balance
from coin_usage.coins.models import Coin


class CoinField(serializers.SlugRelatedField):
    """A custom field for the coin field."""

    def get_queryset(self):
        """Get the queryset for the field."""
        return Coin.objects.all()


class BalanceModelSerializer(serializers.ModelSerializer):
    """Balance model serializer."""

    coin = CoinField(required=True, slug_field="ticker_symbol")
    amount = serializers.FloatField()

    def validate_amount(self, value):
        """Validate the amount."""
        if value < 0:
            raise serializers.ValidationError(_("Amount cannot be negative."))
        return value

    class Meta:
        """Meta class."""

        model = Balance
        fields = ("coin", "amount")
