from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from conversion.serializer import CurrencyConverterSerializer
from conversion.utils import *


class CurrencyConverterViewSet(viewsets.ViewSet):
    '''API endpoint para realizar conversões de moeda.'''

    #Definição da classe serialiadora e dos métodos HTTP permitidos
    serializer_class = CurrencyConverterSerializer                                
    http_method_names = ['get', 'post']


    # Armazena a resposta da view em cache por uma hora
    @method_decorator(cache_page(3600)) 
    def dispatch(self, *args, **kwargs):
        '''ViewSet dispatch method com cache por uma hora.'''                                                                                                                
        return super(CurrencyConverterViewSet, self).dispatch(*args, **kwargs)
    

    #Método GET para lidar com a conversão de moedas na URL
    def get(self, request):
        '''Manipula solicitações GET para conversão de moedas'''

        # Extrai os parâmetros da URL de requisição
        from_currency = request.GET.get('from', '').upper()
        to_currency = request.GET.get('to', '').upper()
        amount = float(request.GET.get('amount', 0))
        

        # Certifica-se de que a conversão de moeda ocorra entre moedas distintas
        if from_currency == to_currency:
            return Response({'error': 'A moeda de origem deve ser diferente da moeda final'}, status=status.HTTP_400_BAD_REQUEST)
        

        # Garante que a entrada seja do tipo numérico adequado para realizar a conversão.
        try:
            amount = float(amount)
        except ValueError:
            return Response({'error': 'O valor a ser convertido deve ser um número válido. Utilize o ponto como separador de números decimais'}, status=status.HTTP_400_BAD_REQUEST)

        
        # Validação da entrada dos parâmetros: moeda de origem, valor a ser convertido e moeda final
        if not from_currency or not to_currency or amount <= 0:
            return Response({'error': 'A requisição deve receber moeda de origem, moeda final e um valor válido.'}, status=status.HTTP_400_BAD_REQUEST)
        

        # Conversão da moeda e retorno da resposta com os resultados obtidos
        response_data = perform_currency_conversion(from_currency, to_currency, amount)
        return Response(response_data)
    


    # Método CREATE para lidar com a conversão de moedas em POST
    def create(self, request):
        '''Manipula solicitações POST para conversão de moedas'''

        #cria uma instância do serializador utilizando os dados fornecidos na requisição
        serializer = CurrencyConverterSerializer(data=request.data)


        # Verifica se a instância do serializador é válida
        if serializer.is_valid():

            # Extrai os parâmetros da requisição do serializador
            from_currency = serializer.validated_data['from_currency'].upper()
            to_currency = serializer.validated_data['to_currency'].upper()
            amount = serializer.validated_data['amount']


            # Certifica-se de que a conversão de moeda ocorra entre moedas distintas
            if from_currency == to_currency:
                return Response({'error': 'A moeda de origem deve ser diferente da moeda final'}, status=status.HTTP_400_BAD_REQUEST)
            

            # Validação da entrada dos parâmetros: moeda de origem, valor a ser convertido e moeda final
            if not from_currency or not to_currency or amount <= 0:
                return Response({'error': 'A requisição deve receber moeda de origem, moeda final e um valor válido.'}, status=status.HTTP_400_BAD_REQUEST)


            # Garante que a entrada seja do tipo numérico adequado para realizar a conversão.
            try:
                amount = float(amount)
            except ValueError:
                return Response({'error': 'O valor a ser convertido deve ser um número válido. Utilize o ponto como separador de números decimais'}, status=status.HTTP_400_BAD_REQUEST)


            # Conversão da moeda e retorno da resposta com os resultados obtidos
            response_data = perform_currency_conversion(from_currency, to_currency, amount)
            return Response(response_data)
        

        # Retorna o erro caso a instância do serializador não seja válida
        else:
            return Response({'error': f'O seguinte erro ocorreu durante a solicitação: {serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)

        