from director1 import dictionar

def test2(d: dict) -> str: 
    for k, v in d.items():
        print(f'Tara {k} are capitala {v}')
        

if __name__ == '__main__':
    rezultat = test2(dictionar)
    print(rezultat)