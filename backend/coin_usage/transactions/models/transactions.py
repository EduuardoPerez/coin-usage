"""Transactions models."""
from django.db.models import PROTECT, FloatField, ForeignKey
from django.utils.translation import gettext_lazy as _

from coin_usage.utils.models import BaseModel


class Transaction(BaseModel):
    """Transactions model.

    Represent the transaction made when a user send coins to other.
    """

    account_from = ForeignKey(
        "accounts.Account", on_delete=PROTECT, verbose_name=_("account_from"), related_name="transactions_from"
    )
    account_to = ForeignKey(
        "accounts.Account", on_delete=PROTECT, verbose_name=_("account_to"), related_name="transactions_to"
    )
    coin = ForeignKey("coins.Coin", on_delete=PROTECT, verbose_name=_("coin"), related_name="transactions")
    amount = FloatField(verbose_name=_("amount"))
