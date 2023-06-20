def test():
    print('hello')

    def interior():
        print("world")

    return interior

temp = test # atribuim functia ca valoare la variabila

temp()()