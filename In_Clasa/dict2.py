# dictionar = {}

# for i in range(10):
#     dictionar[str(i)] = i

# print(dictionar['0'])

# dict comprehension

dictionar = {}

for i in range(10):
    dictionar[str(i)] = i

dictionar = {str(i): i for i in range(20) if i % 2 == 0 or i % 5 != 0} # if este pentru doar valorile pare si nu divizibile cu 5
dictionar = {str(i): i for i in range(20) if i % 2 == 0 if i % 5 == 0} # if este pentru doar valorile pare si divizibile cu 5

print(dictionar)