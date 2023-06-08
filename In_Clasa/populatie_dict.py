import requests

response = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')

data = response.json()['data']

data = [item['Population'] for item in data ][::-1] # extragem din data numai populatia si o inversam

calculat = []
statistica = {}
primul_an = 2013
for i in range(len(data) - 1): # -1 se pune pentru nu a obtine out of range
    diferenta = data[i + 1] - data[i]
    anul = f'{primul_an + i} - {primul_an + i + 1} ' # se face pentru a pune 2013 - 2014

    statistica[anul] = diferenta
    calculat.append(diferenta)

print('Modificarea pe an: ', sum(calculat) / len(calculat))

for k, v in statistica.items():
    print(f"Diferenta anului: {k} - {v}")



