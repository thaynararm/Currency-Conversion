from rest_framework import serializers
from conversion.models import Currency

#Definição dos campos que serão exibidos na API
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'