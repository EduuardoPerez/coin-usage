"""Accounts serializers."""
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from coin_usage.accounts.models import Account, Balance
from coin_usage.exceptions import InsufficientFunds
from coin_usage.transactions.models import Transaction

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

    @transaction.atomic()
    def update(self, instance, validated_data):
        """Update the account balance."""
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


class SendCoinSerializer(serializers.ModelSerializer):
    """Send coin from account serializer."""

    address = serializers.CharField()
    balance = BalanceModelSerializer()

    def validate(self, attrs):
        """Validate if user has a balance for the coin."""
        super().validate(attrs)
        user = self.context["user"]
        if user.account.address == attrs.get("address"):
            raise serializers.ValidationError(_("You can't send to yourself."))
        try:
            user.account.balances.get(coin=attrs.get("balance").get("coin"))
        except Balance.DoesNotExist:
            raise serializers.ValidationError(_("User does not have a balance for this coin"))
        return attrs

    @transaction.atomic()
    def update(self, instance, validated_data):
        """Update the accounts balance."""
        coin = validated_data.get("balance").get("coin")
        amount = validated_data.get("balance").get("amount")
        try:
            account_to = Account.objects.get(address=validated_data.get("address"))
        except Account.DoesNotExist:
            raise serializers.ValidationError(_("Account not found"))
        try:
            balance_to = account_to.balances.get(coin=coin)
        except Balance.DoesNotExist:
            try:
                instance.balances.get(coin=coin).withdraw(amount)
                new_balance = Balance.objects.create(account=account_to, **validated_data.get("balance"))
                account_to.balances.add(new_balance)
                account_to.save()
                Transaction.objects.create(
                    account_from=instance,
                    account_to=account_to,
                    coin=coin,
                    amount=amount,
                )
                return instance
            except InsufficientFunds:
                raise serializers.ValidationError(_("Insufficient funds"))
        else:
            try:
                instance.balances.get(coin=coin).withdraw(amount)
                balance_to.deposit(amount)
                Transaction.objects.create(
                    account_from=instance,
                    account_to=account_to,
                    coin=coin,
                    amount=amount,
                )
                return instance
            except InsufficientFunds:
                raise serializers.ValidationError(_("Insufficient funds"))

    class Meta:
        """Meta class."""

        model = Account
        fields = ("address", "balance")
