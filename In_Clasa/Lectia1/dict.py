# dictionar = {
#     1: 'Adevarat',
#     3.14: 'Fals',
# }

# print(dictionar[1])
# print(dictionar[3.14])
# print(len(dictionar)) # numara elementele 
# print(sorted(dictionar)) # creaza o lista din key
# print(dictionar.keys()) # prineaza keile
# print(dictionar.values()) # printeaza valorile

# set default

# dictionar.setdefault(40, 'test')

# dictionar[40] = 'Aici avem o valoare'
adresa = {
    'oras': 'RO',
    'strada': 'Brasov',
    'cod_postal': '2012',
    'tara': 'bd. Libertatii',
}

print(adresa)

# keys
for k in adresa:
    print(k)
print()

# values
for v in adresa:
    print(v)
print()