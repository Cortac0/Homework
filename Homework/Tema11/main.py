from file import *
from tools import *

phonebook = read_phonebook()

print('''
    l - Enumerate person
    w - Add new entries
    f - Search by full name
    p - Searh by telephone number or city
    d - Deletee a record for a given telephone number
    b - Exit program
''')
try:
    while True:
        print('=' * 40)
        command = input("Introdu o comanda (l, w, f, b, p, d): ")
        if command == 'l': # citim lista
            for i, person in enumerate(phonebook.keys()):
                print(f"{i+1} - {person}")

        if command == 'w': # add new entries
            first_name = input("introdu first_name: ")
            last_name = input("introdu first_name: ")
            phonebook[first_name][last_name] = {
                'tel': input("Numar de telefon: "),
                'oras': input("Oras: ")
            }
        elif command == 'f': # search by full name
            phonebook_reader(phonebook)
        elif command == 'p': # search by telephone number or sity
            params = {
                1: 'tel',
                2: 'oras'
            }
            parametru = int(input("Alege parametrul de cautare (1 - tel, 2 - oras): "))
            value = input("Care este valoarea parametrului?: ")

            for k, v in phonebook.items():
                if value == v[params[parametru]]:
                    print(f"Persoana este: {k}")
        elif command == 'd': # deletee a record for a given telephone number
            tel = input("Introdu numarul: ")

            for k, v in list(phonebook.items()):
                if v['tel'] == tel:
                    del phonebook[k]
                    print(f"Persoana cu numarul {tel} a fost stersa!")
                    break
        elif command == 'b': # break the program
            break
except KeyboardInterrupt:
    write_phonebook(phonebook)