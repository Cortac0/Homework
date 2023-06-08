import json

dictionar = {str(i): i for i in range(20)}

file = open('out.json', mode='w')

with open('out.json', mode='w') as file:
    file.write(json.dumps(dictionar))

print(file)

