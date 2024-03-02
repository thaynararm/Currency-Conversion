from rest_framework import serializers

class CurrencyConverterSerializer(serializers.Serializer):
    from_currency = serializers.CharField(max_length=3, required=True)
    to_currency = serializers.CharField(max_length=3, required=True)
    amount = serializers.FloatField(required=True)
