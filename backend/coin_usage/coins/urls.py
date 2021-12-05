"""Coins URLs."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

# Views
from .views import coins as coin_views

router = DefaultRouter()
router.register(r"coins", coin_views.CoinViewSet, basename="coin")

urlpatterns = [path("", include(router.urls))]
