import random

# generarea unei lise
lista = list(range(10))
print(f'Lista este {lista}')

# prin random.simple
lista_random = random.sample(lista, k=3)
print(f'Lista random este {lista_random}')

# cu functia shuffle
random.shuffle(lista)
print(f'Lista random este {lista}')

print('hmm')