from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from conversion.utils import *


class CurrencyConverterView(APIView):

    # Armazena a resposta da view em cache por uma hora
    @method_decorator(cache_page(3600)) 
    def dispatch(self, *args, **kwargs):                                                                                                                
        return super(CurrencyConverterView, self).dispatch(*args, **kwargs)
    
    # Método GET para lidar com a conversão de moedas 
    def get(self, request):

        #Extração dos parâmetros da URL de requisição
        from_currency = request.GET.get('from', '').upper()
        to_currency = request.GET.get('to', '').upper()
        amount = float(request.GET.get('amount', 0))
        
        # Validação da entrada do valor a ser convertido para float
        try:
            amount = float(amount)
        except ValueError:
            return Response({'error': 'O valor a ser convertido deve ser um número válido. Utilize o ponto como separador de números decimais'}, status=status.HTTP_400_BAD_REQUEST)
        

        # Validação da entrada dos parâmetros: moeda de origem, valor a ser convertido e moeda final
        if not from_currency or not to_currency or amount <= 0:
            return Response({'error': 'A requisição deve receber moeda de origem, moeda final e um valor válido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        response_data = perform_currency_conversion(from_currency, to_currency, amount)

        return Response(response_data)


