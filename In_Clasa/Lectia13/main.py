
def test():
    print('hello')

    def interior():
        print("world")

    return interior

temp = test # atribuim functia ca valoare la variabila

temp()()

# print(dir(test())) # dir (pentru a vedea optiunile pentru functie)