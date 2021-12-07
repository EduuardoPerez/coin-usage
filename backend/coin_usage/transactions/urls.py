"""Transactions urls."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import transactions as transactions_views

router = DefaultRouter()
router.register(r"transactions", transactions_views.TransactionViewSet, basename="transactions")

urlpatterns = [path("", include(router.urls))]
