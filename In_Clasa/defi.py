

# def test(x: int, text='Hello') -> str: # (->) tipul de date pe care urmeaza sa-l transcrim in functie
#     print('X este:', x)
#     print('Textul este:', text)
    
#     return str(x) + text    

# if __name__ == '__main__': # se pune pentru sa se execute functia in alt fisier ( from def import main)
#     Rezultat = test(9, 'Hello') # trebuie de respectat ordinea argumentelor pozitionale
#     print('Rezultatul este:', Rezultat)

# pozitional arguments (args)
# keyword arguments (kwargs) - creaza un dictionar
# def function(args, kwards) trebuie de respectat ca sa nu obtine eroare.
# unpacking arguments (*, **)

# def test2(*args, **kwargs) -> str: # pentru a defini toate argumentele
#     print('args:',args)
#     print('kwargs:',kwargs)

# for i, item in enumerate([1, 2, 3]):

# if __name__ == '__main__':
#     rezultat = test2(2, 3, text='Acesta este un test', f=1.9)
#     print('Rezultatul este:', rezultat)

#     lista = [1, 2, 3]
#     print(lista, *lista)
#     print(lista[0], lista[1], lista[2]) # cum functioneaza (*)

#     dictionar = {'sep': '//', 'end': ']]'}
#     print(1, 3, 5, **dictionar)
    
# ##########
# def test2(x, *args, text='Hello', **kwargs) -> str: 
#     print('args:', x, args)
#     print('kwargs:', text, kwargs)
    
# if __name__ == '__main__':    
#     rezultat = test2(2, 3, text='Acesta este un test', f=1.9)
#     print('Rezultatul este:', rezultat)

############
# def test2(x, *args, text='Hello', **kwargs) -> str: 
#     if 'f' in kwargs: # pentru a verifica daca cheia exista in dictionar
#         print(kwargs['f'])
#         return 
#     return 'string'
    
# if __name__ == '__main__':    
#     rezultat = test2(2, 3, text='Acesta este un test', f=1.9)
#     print('Rezultatul este:', rezultat)
##############
# if __name__ == '__main__':    
#     for j in iterator(5):
#         print(f'Se executa functia a {j} oara') # se executa cu yield din fori.py
#     # rezultat = iterator(5)
#     # print('Rezultatul este:', rezultat)
##############
# def test():
#     def _proprie():
#         print('Functia interioara')

# if __name__ == '__main__': 
#     rezultat = test()
#     print('Rezultatul este:', rezultat)

dictionar = {
    'Moldova': 'Chisinau',
    'Romania': 'Bucuresti',
    'Italia': 'Roma',
}

