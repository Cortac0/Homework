import json


with open('out.json', mode='r') as file:
    dictionar = json.loads(file.read())

print(dictionar)
print(dictionar['0'])