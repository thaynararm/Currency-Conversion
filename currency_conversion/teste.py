from_currency = 'BTC'
to_currency = 'ETH'
amount = 10
import requests


def get_data_API() -> dict:
    url = 'https://cdn.moeda.info/api/latest.json'
    r = requests.get(url).json()
    quotes = r.items()

    return quotes


def get_value() -> float:
    
    price = dict(get_data_API())
    
    if from_currency == 'USD':
        valor = amount * price['rates'][to_currency]
        print(valor)

    elif to_currency == 'USD':
        valor = amount/price['rates'][from_currency]
        print(valor)

    else:
        usd = amount/price['rates'][from_currency]
        valor = usd * price['rates'][to_currency]

        print(valor)
