"""Coins model admin."""
from django.contrib import admin

from coin_usage.coins.models import Coin


@admin.register(Coin)
class CustomCoinAdmin(admin.ModelAdmin):
    """Account model admin."""

    list_display = ("ticker_symbol", "name")
    list_filter = ("ticker_symbol", "name", "created", "modified")
