"""Balances model."""
from django.db import transaction
from django.db.models import CASCADE, FloatField, ForeignKey
from django.utils.translation import gettext_lazy as _

from coin_usage.exceptions import InsufficientFunds, InvalidAmount
from coin_usage.utils.models import BaseModel


class Balance(BaseModel):
    """Balance model.

    Represent the balance of a coin for an user.
    """

    coin = ForeignKey("coins.Coin", on_delete=CASCADE, verbose_name=_("coin"), related_name="balances")
    account = ForeignKey("accounts.Account", on_delete=CASCADE, verbose_name=_("account"), related_name="balances")
    amount = FloatField(verbose_name=_("amount"))

    def get_queryset(self):
        """Get the queryset."""
        return self.__class__.objects.filter(id=self.id)

    @transaction.atomic()
    def deposit(self, amount):
        """Deposit the amount."""
        if amount <= 0:
            raise InvalidAmount()
        balance = self.get_queryset().select_for_update().get()
        balance.amount += amount
        balance.save()
        return balance.amount

    @transaction.atomic()
    def withdraw(self, amount):
        """Withdraw the amount."""
        if amount <= 0:
            raise InvalidAmount()
        balance = self.get_queryset().select_for_update().get()
        if amount > balance.amount:
            raise InsufficientFunds()
        balance.amount -= amount
        balance.save()
        return balance.amount

    class Meta:
        """Meta class."""

        db_table = "balance"
        verbose_name = _("balance")
        verbose_name_plural = _("balances")
        unique_together = ("coin", "account")
        ordering = ["account", "coin"]
