import requests

from_currency = 'USD'
to_currency = 'EUR'
code = f'{from_currency}{to_currency}'
amount = 10

def extração_url() -> dict:
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,USD-EUR,BRL-USD,BRL-EUR,EUR-USD,EUR-BRL,BTC-USD,BTC-EUR,BTC-BRL,ETH-USD,ETH-EUR,ETH-BRL'
    r = requests.get(url).json()
    quotes = r.items()

    return quotes


def valor_cotacoes() -> dict:
    
    quotes = dict(extração_url())
    quotes_keys = quotes.keys()
    
    price = {key: float(quotes[key]['bid']) for key in quotes_keys}

    chaves_sem_cotacao = [(chave[3:]+chave[:3]) for chave in quotes_keys if (chave[3:]+chave[:3]) not in quotes_keys]

    for chave in chaves_sem_cotacao:
        chave_calculo = chave[3:]+chave[:3]
        bid_value = 1/(float(quotes[chave_calculo]['bid']))
        dictionary = {chave: bid_value}
        price.update(dictionary)

    return price


list_price = valor_cotacoes()
print(list_price)
#print(quotes_keys)
#print(chaves_sem_cotacao)
#print(quotes)
#print(quotes)


''' 
def inserir_cotacoes_que_existem():
    prices = {}

    for quote, values in extração_url():
        low_value = float(values['bid'])
        dictionary = {quote: low_value}
        prices.update(dictionary)

    return prices

def inserir_cotacoes_nao_existentes():
    no_quotes = {}

    for quote, values in inserir_cotacoes_que_existem().items():
        first = quote[:3]
        last = quote[3:]
        changed = last+first
        

        if changed not in inserir_cotacoes_que_existem().keys():
            value = values
            low_value = 1/value
            new_dictionary = {changed: low_value}
            no_quotes.update(new_dictionary)
            #print(new_dictionary)

    print(inserir_cotacoes_que_existem())
    #print(no_quotes)
    inserir_cotacoes_que_existem().update(no_quotes)
    #print(prices)
    #print(prices)

    return inserir_cotacoes_que_existem()

    

if code in inserir_cotacoes_nao_existentes():
    price = inserir_cotacoes_nao_existentes()[code]
    converted_amount = amount * price

    #print(f'from_currency: {from_currency}  \nto_currency: {to_currency} \namount: {amount} \nprice: {price} \nconverted_amount: {converted_amount}')

else:
    pass
    #print('não tem')



'''
