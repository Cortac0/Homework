
def iterator(n):
    for i in range(n):
        # if i % 2 == 0:
            # continue # se foloseste pentru a continua iteratia
            print(f'Suntem la iteratia {i}')
            yield i  # yield returneaza rezultatul iteratiei curente
