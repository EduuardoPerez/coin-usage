"""Coin model."""
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from coin_usage.utils.models import BaseModel


class Coin(BaseModel):
    """Coin model.

    Represent the coin entity.s
    """

    ticker_symbol = CharField(
        max_length=5, unique=True, error_messages={"unique": _("A coin with that ticker symbol already exists.")}
    )
    name = CharField(max_length=50)

    def __str__(self):
        """Return the coin ticker symbol and name."""
        return f"({self.ticker_symbol}) {self.name}"

    class Meta:
        """Meta class."""

        ordering = ["ticker_symbol"]
        verbose_name = "coin"
