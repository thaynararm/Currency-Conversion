import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL,USD-EUR,BRL-USD,BRL-EUR,EUR-USD,EUR-BRL,BTC-USD,BTC-EUR,BTC-BRL,ETH-USD,ETH-EUR,ETH-BRL'
r = requests.get(url).json()
quotes = r.items()

from_currency = 'USD'
to_currency = 'EUR'
code = f'{from_currency}{to_currency}'
amount = 10

prices = {}

for quote, values in quotes:
    low_value = float(values['bid'])
    dictionary = {quote: low_value}
    prices.update(dictionary)

no_quotes = {}

for quote, values in prices.items():
    first = quote[:3]
    last = quote[3:]
    changed = last+first
    

    if changed not in prices.keys():
        value = values
        low_value = 1/value
        new_dictionary = {changed: low_value}
        no_quotes.update(new_dictionary)
        #print(new_dictionary)

print(prices)
#print(no_quotes)
prices.update(no_quotes)
print(prices)
#print(prices)

    

if code in prices:
    price = prices[code]
    converted_amount = amount * price

    #print(f'from_currency: {from_currency}  \nto_currency: {to_currency} \namount: {amount} \nprice: {price} \nconverted_amount: {converted_amount}')

else:
    pass
    #print('não tem')



