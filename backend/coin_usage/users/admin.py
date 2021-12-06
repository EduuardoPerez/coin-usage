"""Users model admin."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from coin_usage.users.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ("email", "username", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff",)


admin.site.register(User, CustomUserAdmin)
