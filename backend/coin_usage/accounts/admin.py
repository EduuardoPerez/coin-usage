"""Accounts admin."""
from django.contrib import admin
from django.contrib.admin import display

from coin_usage.accounts.models import Account, Balance


@admin.register(Account)
class CustomAccountAdmin(admin.ModelAdmin):
    """Account model admin."""

    list_display = ("address", "user")
    list_filter = ("address", "user", "created", "modified")


@admin.register(Balance)
class CustomBalanceAdmin(admin.ModelAdmin):
    """Balance model admin."""

    list_display = ("account_user", "account_address", "coin", "amount")
    list_filter = ("coin", "account", "amount", "created", "modified")

    @display()
    def account_user(self, obj):
        """Account user."""
        return obj.account.user

    @display()
    def account_address(self, obj):
        """Account address."""
        return obj.account.address
