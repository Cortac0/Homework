import json

def write_phonebook(data):  
    with open('phonebook.json', 'w') as f: # scriem in fisier
        f.write(json.dumps(data))

def read_phonebook() -> dict:
    try:
        with open('phonebook.json', 'r') as f: # citim din fisier
            data = f.read()
        return json.loads(data)
    except FileNotFoundError:
        return {}

    