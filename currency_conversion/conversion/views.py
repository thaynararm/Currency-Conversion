from rest_framework import viewsets
from conversion.models import Currency
from conversion.serializer import CurrencySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    http_method_names = ['get', 'post', 'patch', 'put']