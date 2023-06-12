# task 1
def oops():
    test_list = [1, 2, 3, 4]
    print(test_list[4])

def corect():
    try:
        oops()
    except IndexError:
        print(KeyError, 'Out of range')  
corect()

# task 2
def num(a, b):
    sqrt = a ** 2
    try:
        valoare = sqrt / b 
        return valoare
    except ZeroDivisionError:
        print('Nu se poate imparti la 0.')
    
try:
    a = float(input('Itrodu valoarea a: '))
    b = float(input('Itrodu valoarea b: '))
    result = num(a, b)
    print(result)
except ValueError:
    print('Nu se accepta str()')
