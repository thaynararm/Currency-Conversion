from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


def get_exchange_rates() -> dict:
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,USD-EUR,BRL-USD,BRL-EUR,EUR-USD,EUR-BRL,BTC-USD,BTC-EUR,BTC-BRL,ETH-USD,ETH-EUR,ETH-BRL'
    r = requests.get(url).json()
    quotes = r.items()

    prices = {}

    for quote, values in quotes:
        low_value = float(values['bid'])
        dictionary = {quote: low_value}
        prices.update(dictionary)

    return prices
    

class CurrencyConverterView(APIView):
    
    def get(self, request):

        #Extração dos parâmetros da URL de requisição
        from_currency = request.GET.get('from', '')
        to_currency = request.GET.get('to', '')
        code = f'{from_currency}{to_currency}'
        amount = float(request.GET.get('amount', 0))

        prices = get_exchange_rates()

        try:
            if code in prices:
                price = prices[code]
                converted_amount = amount * price

                response_data = {
                    'from_currency': from_currency,
                    'to_currency': to_currency,
                    'amount': amount,
                    'converted_amount': converted_amount
                }
            
                return Response(response_data)
        
            return Response({'error': 'Código de moeda não encontrado'}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': f'Ocorreu um erro: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





