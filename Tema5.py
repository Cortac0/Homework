# task 1
import random

correct = False

while not correct:
    calculator = random.randint(1, 5)
    numar = int(input('Introdu un numar: '))

    if numar == calculator:
        correct = True
        print('Corect')
    else:
        print(f'Gresit, numarul este {calculator}')


# task 2
name = input('Name: ')
age = int(input('Age: '))

print(f"Hello {name}, o your next birthday you'll be {age + 1} years.")

## task 3
# user = list(input('Scrie un cuvant: '))

# print(user.)



# task 4

a = 5
b = 3
c = a * b

user = int(input("Cat o sa fie 5 * 3 = "))

if user == c:
    print("Corect")
else:
    print(f"Gresit, raspunsul este {c}")


