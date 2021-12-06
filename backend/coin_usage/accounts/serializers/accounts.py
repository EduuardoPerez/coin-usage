"""Accounts serializers."""
from rest_framework import serializers

from coin_usage.accounts.models import Account, Balance

from .balances import BalanceModelSerializer


class AccountModelSerializer(serializers.ModelSerializer):
    """Account model serializer."""

    balances = BalanceModelSerializer(many=True)

    class Meta:
        """Meta class."""

        model = Account
        fields = ("address", "balances")


class DepositCoinSerializer(serializers.ModelSerializer):
    """Deposit coin into account serializer."""

    balance = BalanceModelSerializer()

    def update(self, instance, validated_data):
        """Update the instance."""
        # breakpoint()
        try:
            balance = instance.balances.get(coin=validated_data.get("balance").get("coin"))
        except Balance.DoesNotExist:
            new_balance = Balance.objects.create(account=instance, **validated_data.get("balance"))
            instance.balances.add(new_balance)
            instance.save()
            return instance
        else:
            balance.deposit(validated_data.get("balance").get("amount"))
            return instance

    class Meta:
        """Meta class."""

        model = Account
        fields = ("balance",)
