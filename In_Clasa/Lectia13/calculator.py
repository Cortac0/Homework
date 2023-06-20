
# exemplu

def add(a, b) -> int:
    print("Adunare")
    return a + b

def minus(a, b):
    return a - b

def calc(operation, a, b):
    ops = {
        'add': add,
        'minus': minus,
    }

    return ops[operation](a, b)

# print(calc('add', 1, 2))

# mapping

# add.__call__(1, 2) # apelarea functiei intr-un mod mai abstract
# print(add.__dir__()) 
# print('-' * 40)
# print(dir())

x = 2
test = '1234567'
print(eval(test)) # evaluarea care tip de date contine un str