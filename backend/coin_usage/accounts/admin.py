"""Accounts admin."""
from django.contrib import admin

from coin_usage.accounts.models import Account


@admin.register(Account)
class CustomCoinAdmin(admin.ModelAdmin):
    """Account model admin."""

    list_display = ("address", "user")
    list_filter = ("address", "user", "created", "modified")
