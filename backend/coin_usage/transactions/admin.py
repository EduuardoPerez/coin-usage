"""Transactions admin."""
from django.contrib import admin

from coin_usage.transactions.models import Transaction


@admin.register(Transaction)
class CustomTransactionAdmin(admin.ModelAdmin):
    """Account model admin."""

    list_display = ("created", "account_from", "account_to", "coin", "amount")
    list_filter = ("account_from", "account_to", "coin", "amount", "created", "modified")
