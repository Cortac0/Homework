def calc(operation, a, b):
    funcs = {
        "add": lambda a, b: a + b,
        "subsract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
    }

arg = calc.__code__.co_flags

print(f"Funcia calc() are {arg} argumente.") # indica cate argumente avem intr-o functie 