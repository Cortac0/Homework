from file import *
from tools import *

phonebook = read_phonebook()

try:
    while True:
        print('=' * 40)
        command = input('Introduceti o comanda (w, l, r, u, d, s): ')

        if command == 'w':
            np = input('Introduce NP: ')
            phonebook[np] = {
                'tel': input('Numar de telefon: '),
                'oras': input('oras: '),
            }
        elif command == 'l': # cate pers. avem
            for i, person in enumerate(phonebook.keys()):
                print(f'{i+1} - {person}')
        elif command == 'r': # citim numele
            phonebook_reader(phonebook)
        elif command == 'u': # updatam datele
            phonebook_update(phonebook)
        elif command == 'd': # stergem datele
            try:
              name = input('Numele persoanei: ')
              phonebook[name]
            except KeyError:
                print("Aceasta persoana nu exista!")
            else:
                del phonebook[name]
        elif command == 's': # cautam dupa tel si oras
            params = {
                1: 'tel',
                2: 'oras',
            }
            parametru = int(input("Alege parametrul de cautare (1 - tel, 2 - oras): "))
            value = input("Care este valoarea parametrului? ")

            for k, v in phonebook.items():
                if value == v[params[parametru]]:
                    print(f"Persoana este: {k}")

           
except KeyboardInterrupt:
    write_phonebook(phonebook)

# conditional lifecycle

