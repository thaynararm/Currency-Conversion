import requests
from rest_framework.response import Response
from rest_framework import status


# Acesso à API de taxas de câmbio
def get_data_API() -> dict:
    '''Retorna o json da API de taxas de câmbio'''
    
    url = 'https://cdn.moeda.info/api/latest.json'

    try:
        response = requests.get(url).json()
        quotes = response.items()
    
    except requests.exceptions.RequestException as e:
        return {'error': f'Erro ao obter as taxas de câmbio: {e}'}

    return quotes


# Lógica de conversão
def perform_currency_conversion(from_currency, to_currency, amount) -> dict:
    '''Realiza a conversão da moeda'''

    # Obtém as taxas de câmbio
    price = dict(get_data_API())

    #Realiza a conversão de moeda
    if from_currency != to_currency:
        
        usd = amount/price['rates'][from_currency]
        value = usd * price['rates'][to_currency]

        # Retorna o resultado convertido
        response_data = {
            'from_currency': from_currency,
            'to_currency': to_currency,
            'amount': amount,
            'converted_amount': value
        }
        
        return response_data
        
    return Response({'error': 'A moeda de origem deve ser diferente da moeda final'}, status=status.HTTP_400_BAD_REQUEST)

