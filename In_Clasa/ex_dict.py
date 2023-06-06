orase = ['Chisinau', 'Iasi', 'Brasov', 'Bucuresti']
distante = [12, 150, 400, 600]

dictionar = {}

# cu enumerate
for i, item in enumerate(orase):
    dictionar[item] = distante[i]
print(dictionar)

# cu zip
for i, j in zip(orase, distante):
    print(i, j)

# cu 2 for
for oras in orase:
    dictionar[oras] = 0

for i, k in enumerate(dictionar):
    dictionar[k] = distante[i]

print(dictionar)
