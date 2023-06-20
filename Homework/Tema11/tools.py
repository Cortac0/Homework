def phonebook_reader(phonebook: dict):
    name = input("numele persoanei: ")
    try:
        print(f"Tel - {phonebook[name]['tel']}")
        print(f"Oras - {phonebook[name]['oras']}")
    except KeyError:
          print("Nu am gasit aceasta persoana, insa avem cateva sugestii!")
    index = 0
    for person in phonebook.keys():
        if name in person:
            index += 1
            print(f"{index} - {person}")
        

def phonebook_update(phonebook):
       try:
              name = phonebook[int(input('Numarul persoanei: '))]
       except KeyError:
              print("Nu exista persoane cu asa numar!")
       else:
              for k, v in name.items(): # update
                     new_value = input(f"Doresti sa modifici: {k} - {v}: ")
                     if new_value:
                            name.update({k: new_value})