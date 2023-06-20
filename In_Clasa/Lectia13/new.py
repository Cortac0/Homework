# lambda

def calc(operation, a, b):
    funcs = {
        "add": lambda a, b: a + b,
        "subsract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        # "divide": lambda a, b: a / b,
    }
    # verificam daca operatia exista sau nu ('divide') cu lambda
    exists = lambda: operation in funcs

    return funcs[operation](a, b) if exists() else "operation does not exist!"
    
taskuri = [
    ("add", 1, 0),
    ("subsract", 5, 4),
    ("multiply", 1, 1),
    ("add", 2, 9),
    ("divide", 2, 9),
]

# cream iterator
# for task in taskuri:
#     print(task, calc(*task))

print(calc.__code__.co_varnames)
print(calc.__code__.co_flags) # indica cate argumente avem intr-o functie

# def add(a, b):
#     return a + b

# test = lambda a, b: a + b # este echivalent cu functia add()

# print(add(1, 2)) # add()
# print(test(1, 2)) # lambda

# numere = [1, 2, 3, 4]

# def functie(x):
#     if x % 2 == 0:
#         return True
#     return False # in loc de else:

# # cu lambda
# print('Cu lambda')
# print(list(filter(
#     lambda x: x % 2 == 0, # va returna un True sau False satatment
#     numere
# )))

# # cu functia
# print('Cu functia')
# print(list(filter(
#     functie,
#     numere
# )))