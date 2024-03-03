import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


def get_data_API() -> dict:
    '''Retorna o json da API de taxas de câmbio'''
    
    url = 'https://cdn.moeda.info/api/latest.json'

    try:
        response = requests.get(url).json()
        quotes = response.items()
    

    except requests.exceptions.RequestException as err:
        raise ValidationError('Erro ao obter as taxas de câmbio: {err}')

    return quotes



def perform_currency_conversion(from_currency, to_currency, amount) -> dict:
    '''Realiza a conversão da moeda'''

    # Obtém as taxas de câmbio
    exchange_rates = dict(get_data_API())

    from_currency, to_currency, amount = validate_currency_params(from_currency, to_currency, amount, exchange_rates)

    usd = amount/exchange_rates['rates'][from_currency]
    value = round(usd * exchange_rates['rates'][to_currency], 4)

    # Retorna o resultado convertido
    response_data = {
        'From Currency': from_currency,
        'To Currency': to_currency,
        'Amount': amount,
        'Converted amount': value,
        'Last Update': exchange_rates['lastupdate']
    }
    
    return response_data



def validate_currency_params(from_currency, to_currency, amount, exchange_rates):
    '''Verifica e lida com os parâmetros fornecidos'''

    # Garante que a entrada das moedas inicial e final sejam válidas
    valid_currencies = exchange_rates.get('rates', {})
    if from_currency not in valid_currencies or to_currency not in valid_currencies:
        raise ValidationError('A moeda de origem e final devem ser válidas.')


    # Permite que o usuário utilize a vírgula como separador decimal
    if type(amount) == str:
        amount = amount.replace(',', '.')


    # Garante que a entrada do valor seja do tipo numérico adequado para realizar a conversão.
    try:
        amount = float(amount)
    except (ValueError, TypeError):
        raise ValidationError('O valor a ser convertido deve ser um número válido.')


    # Certifica-se de que a conversão de moeda ocorra entre moedas distintas
    if from_currency == to_currency:
        raise ValidationError('A moeda de origem deve ser diferente da moeda final.')
    

    # Validação da entrada dos parâmetros: moeda de origem, valor a ser convertido e moeda final
    if not from_currency or not to_currency:
       raise ValidationError('A requisição deve receber moeda de origem e moeda final.') 
       
    return from_currency, to_currency, amount

quotes = dict(get_data_API())
quotes_moedas = quotes['rates']
print(quotes_moedas.keys())