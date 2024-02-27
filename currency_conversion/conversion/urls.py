from django.urls import path
from conversion.views import CurrencyViewSet

urlpatterns = [
    path('convert_currency/', convert_currency, name='convert_currency'),
]
