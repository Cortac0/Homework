# # task 1
import random

numbers = []
count = 0

while count < 10:
    number = random.randint(1, 100)
    numbers.append(number)
    count += 1
print('Lista generata: ',numbers)

largest = numbers[0]
i = 1

while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1
print('Cel mai mare numar este: ', largest)

# # task 2
lista1 = []
lista2 = []
count1 = 0
count2 = 0
while count1 < 10:
    numar = random.randint(1, 10)
    lista1.append(numar)
    count1 += 1
print('Lista 1: ',lista1)

while count2 < 10:
    numar = random.randint(1, 10)
    lista2.append(numar)
    count2 += 1
print('Lista 2: ',lista2)

lista3 = set(lista1 + lista2)

print('Lista 3 fara duplicate: ',list(lista3))

# task 3
lista = []
count = 0

while count < 100:
    numar = random.randint(1, 100)
    lista.append(numar)
    count += 1
print('Lista',lista)

divizibile_cu_7 = []
i = 0
for i in lista:
    if i & 7 == 0 and i % 5 != 0: 
        divizibile_cu_7.append(i)
print('Divizibile cu 7: ',divizibile_cu_7)

