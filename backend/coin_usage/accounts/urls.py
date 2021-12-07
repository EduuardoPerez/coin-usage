"""Accounts urls."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import accounts as account_views
from .views import balances as balance_views

router = DefaultRouter()
router.register(r"accounts", account_views.AccountViewSet, basename="account")
router.register(r"balances", balance_views.BalanceViewSet, basename="balance")

urlpatterns = [path("", include(router.urls))]
