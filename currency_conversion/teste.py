import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL,USD-EUR,BRL-USD,BRL-EUR,EUR-USD,EUR-BRL,BTC-USD,BTC-EUR,BTC-BRL,ETH-USD,ETH-EUR,ETH-BRL'
r = requests.get(url).json()
quotes = r.items()

from_currency = 'USD'
to_currency = 'EUR'
code = f'{from_currency}{to_currency}'
amount = 10

print(code)

#print(quotes)
prices = {}

for quote, values in quotes:
    low_value = float(values['low'])
    dictionary = {quote: low_value}
    prices.update(dictionary)
    

if code in prices:
    price = prices[code]
    amount = amount * price
    print(amount)

else:
    print('não tem')



