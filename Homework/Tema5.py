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

print(f"Hello {name}, on your next birthday you'll be {age + 1} years.")

# task 3
import random

def create_random_string(input_string):
    random_string = ''.join(random.sample(input_string, len(input_string)))
    return random_string

def generate_random_strings(input_string, num_strings):
    random_strings = []
    for _ in range(num_strings):
        random_strings.append(create_random_string(input_string))
    return random_strings

input_string = input("Enter a string: ")
random_strings = generate_random_strings(input_string, 5)

print("Random strings:")
for string in random_strings:
    print(string)

# task 4

a = 5
b = 3
c = a * b

user = int(input("Cat o sa fie 5 * 3 = "))

if user == c:
    print("Corect")
else:
    print(f"Gresit, raspunsul este {c}")