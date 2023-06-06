import requests, json

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

data = response.json()

# with open('data.json', 'w') as f:
#     f.write(json.dumps(data)) # converteste dictionarul intr-un string

# cream un covertor
try: # se face pentru ca daca userul introduce un str.
    cantitatea  = float(input('Introdu cantitatea pentru conversie: '))
except ValueError:
    print('Cantitatea trebuie sa fie un numar!')
    cantitatea = float(input('Introdu cantitatea pentru conversie: '))
valuta = input('introdu valuta: ').upper()

if valuta not in ['USD', 'EUR', 'GBP']:
    valuta = input('sunt disponibile numai USD, EUR, GBP')

valuta = valuta.upper()

pret = data['bpi'][valuta]['rate_float']

conversia = cantitatea * pret

print(f'{cantitatea} Bitcoin = {conversia} {valuta}')

