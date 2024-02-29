from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


def get_data_API() -> dict:
    url = 'https://cdn.moeda.info/api/latest.json'
    r = requests.get(url).json()
    quotes = r.items()

    return quotes

class CurrencyConverterView(APIView):
    
    def get(self, request):

        #Extração dos parâmetros da URL de requisição
        from_currency = request.GET.get('from', '').upper()
        to_currency = request.GET.get('to', '').upper()
        amount = float(request.GET.get('amount', 0))
        
        try:
            amount = float(amount)
        except ValueError:
            return Response({'error': 'O valor a ser convertido deve ser um número válido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not from_currency or not to_currency or amount <= 0:
            return Response({'error': 'A requisição deve receber moeda de origem, moeda final e um valor válido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        price = dict(get_data_API())

        if from_currency != to_currency:
            if from_currency == 'USD':
                value = amount * price['rates'][to_currency]

            elif to_currency == 'USD':  
                value = amount/price['rates'][from_currency]

            else:
                usd = amount/price['rates'][from_currency]
                value = usd * price['rates'][to_currency]

            response_data = {
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount,
                'converted_amount': value
            }
            
            return Response(response_data)
            
        return Response({'error': 'A moeda de origem deve ser diferente da moeda final'}, status=status.HTTP_400_BAD_REQUEST)





