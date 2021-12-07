"""Transactions admin."""
from django.contrib import admin
from django.contrib.admin import display

from coin_usage.transactions.models import Transaction


@admin.register(Transaction)
class CustomTransactionAdmin(admin.ModelAdmin):
    """Account model admin."""

    list_display = ("created", "get_account_from", "get_account_to", "coin", "amount")
    list_filter = ("account_from", "account_to", "coin", "amount", "created", "modified")

    @display()
    def get_account_from(self, obj):
        """Account from."""
        return obj.account_from.address

    @display()
    def get_account_to(self, obj):
        """Account to."""
        return obj.account_to.address
