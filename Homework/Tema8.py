# task 1
# def favorite_movie(movie):
#     print(f'Filmul meu preferat se numeste "{movie}"')
# favorite_movie('Prey')

# task 2
# def test2(d: dict) -> str: 
#     for k, v in d.items():
#         print(f'Tara {k} are capitala {v}')
        

# dictionar = {
#     'Moldova': 'Chisinau',
#     'Romania': 'Bucuresti',
#     'Italia': 'Roma',
# }
 
# if __name__ == '__main__':
#     rezultat = test2(dictionar)
#     print(rezultat)

# task 3
def make_operation(operation, *args):
    arg = list(args)
    total = 0
    operation = args.pop(0)
    
    for num in args:
        if operation == '-':
            total -= num
        elif operation == '+':
            total += num
    else:
        total * num
    return total

print(make_operation(7, 7, 2))  
  

    


