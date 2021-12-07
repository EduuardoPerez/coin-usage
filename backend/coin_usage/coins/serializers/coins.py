"""Coins serializers."""
from rest_framework import serializers

from coin_usage.coins.models import Coin


class CoinModelSerializer(serializers.ModelSerializer):
    """Coin model serializer."""

    class Meta:
        """Meta class."""

        model = Coin
        fields = ("ticker_symbol", "name")
