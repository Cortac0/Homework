def phonebook_reader(phonebook: dict):
       name = input('Numele persoanei: ')
       try:
              print(f'Tel - {phonebook[name]["tel"]}')
              print(f'Oras - {phonebook[name]["oras"]}')
       except KeyError:
              print('Nu am gasit aceasta persoana, insa avem cateva sugestii.')
       index = 0
       for person in phonebook.keys():
              if name in person:
                     index += 1
                     print(f'{index} - {person}')

def phonebook_update(phonebook):
       try:
              person = phonebook[input('Numele persoanei: ')]
       except KeyError:
              print("Aceasta persoana nu exista!")
       else:
              for k, v in person.items(): # update
                     new_value = input(f"Doresti sa modifici: {k} - {v}: ")
                     if new_value:
                            person.update({k: new_value})

       
