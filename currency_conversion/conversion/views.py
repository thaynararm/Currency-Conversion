from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


def get_data_API() -> dict:
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,USD-EUR,BRL-USD,BRL-EUR,EUR-USD,EUR-BRL,BTC-USD,BTC-EUR,BTC-BRL,ETH-USD,ETH-EUR,ETH-BRL'
    r = requests.get(url).json()
    quotes = r.items()

    return quotes


def get_exchange_rates() -> dict:
    
    quotes = dict(get_data_API())
    quotes_keys = quotes.keys()
    
    price = {key: float(quotes[key]['bid']) for key in quotes_keys}

    chaves_sem_cotacao = [(chave[3:]+chave[:3]) for chave in quotes_keys if (chave[3:]+chave[:3]) not in quotes_keys]

    for chave in chaves_sem_cotacao:
        chave_calculo = chave[3:]+chave[:3]
        bid_value = 1/(float(quotes[chave_calculo]['bid']))
        dictionary = {chave: bid_value}
        price.update(dictionary)

    return price
    

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





