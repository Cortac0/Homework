def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def calc(operation, a, b):
    return f[operation](a, b)

f = {}
for item in dir(): # trecerea prin toatee dunder-methods
    print(item)
    if item in ['calc', 'f']: # excludem 'calc' si 'f' din operatii
        print("Nu adaugam")
        continue
    if not '__' in item: # adaugam numai ceea ce nu-i cu dunder_methods
        print("Adaugam")
        f[item] = eval(item)
    else:
        print("Nu adaugam")
print(f)
print(calc('inmultire', 1, 2))

# sau cu lambda
def calc(operation, a, b):
    f = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b
    }
    return f[operation](a, b)

print(calc('add', 1, 2))