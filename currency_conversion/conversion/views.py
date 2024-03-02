from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from conversion.serializer import CurrencyConverterSerializer
from conversion.utils import *


class CurrencyConverterViewSet(viewsets.ViewSet):
    '''Endpoint da API para realizar conversões de moeda.'''

    #Definição da classe serialiadora e dos métodos HTTP permitidos
    serializer_class = CurrencyConverterSerializer                                
    http_method_names = ['get', 'post']


    @method_decorator(cache_page(3600)) 
    def dispatch(self, *args, **kwargs):
        '''Método de despacho da ViewSet com cache de 1 hora.'''                                                                                                                
        return super(CurrencyConverterViewSet, self).dispatch(*args, **kwargs)
    

    def get(self, request):
        '''Manipula solicitações GET para conversão de moedas'''

        # Extrai os parâmetros da URL da requisição
        from_currency = request.GET.get('from', '').upper()
        to_currency = request.GET.get('to', '').upper()
        amount = request.GET.get('amount', 0)
        
        # Realiza a conversão de moeda e retorna a resposta com os resultados
        response_data = perform_currency_conversion(from_currency, to_currency, amount)
        return Response(response_data)
    


    def create(self, request):
        '''Manipula solicitações POST para conversão de moedas'''

        # Cria uma instância do serializador usando os dados fornecidos na requisição
        serializer = CurrencyConverterSerializer(data=request.data)


        # Verifica se a instância do serializador é válida
        if serializer.is_valid():

            # Extrai parâmetros dos dados validados do serializador
            from_currency = serializer.validated_data['from_currency'].upper()
            to_currency = serializer.validated_data['to_currency'].upper()
            amount = serializer.validated_data['amount']
            

            # Realiza a conversão de moeda e retorna a resposta com os resultados
            response_data = perform_currency_conversion(from_currency, to_currency, amount)
            return Response(response_data)
        

        # Retorna um erro se a instância do serializador não for válida
        else:
            raise ValidationError('A requisição deve receber moeda de origem, moeda final e valor a ser convertido')
        
        
        