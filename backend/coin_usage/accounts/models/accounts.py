"""Accounts models."""
from django.db.models import CASCADE, CharField, ForeignKey, OneToOneField
from django.utils.translation import gettext_lazy as _

from coin_usage.accounts.managers import AccountsManager
from coin_usage.utils.models import BaseModel


class Account(BaseModel):
    """Accounts model.

    Represent the account with its balance and address of an user.
    """

    address = CharField(max_length=35, unique=True, verbose_name=_("address"))
    user = OneToOneField("users.User", on_delete=CASCADE, verbose_name=_("user"), related_name="account")
    balance = ForeignKey(
        "accounts.Balance", null=True, on_delete=CASCADE, verbose_name=_("balance"), related_name="accounts"
    )

    objects = AccountsManager()

    class Meta:
        """Meta class."""

        verbose_name = _("account")
        verbose_name_plural = _("accounts")
        unique_together = ("user", "address")
