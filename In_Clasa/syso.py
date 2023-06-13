import sys

# sys.exit(0) # fortam programul sa se opreasca
# print(sys.argv) # transofrma intr-un executabil (transmite parametri direct in terminal)

print(sys.argv)
operation = sys.argv[1]

def make_operation(*args):
    args = list(args)

    operation = '-'
    print(operation)

    total = 0
    
    for num in args:
        if operation == '-':
            total -= num
        elif operation == '+':
            total += num
        return total

print(operation)
print(make_operation(5, 5, -10, -20))  
