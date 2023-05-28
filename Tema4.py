# task 1
print('Sample string = "helloworld"')
string = 'helloworld'
expected = string[0:3]
print('Expected string = ',expected+string[-1])
print()
print('Sample string = "my"')
string = 'my'
print('Expected string = ',string*2)
print()
text = 'x'
if len(text) < 2:
    text = ''

print('Expected result:', text)
print()


# task 2
user = int(input("Write a phone number only 10 caracters: "))
len = len(str(user))
if len == 10:
    print("the number is written correctly")
else:
    print("the number is not written correctly")

# task 3
user = input('Name: ')
lower = user.lower()
stored = 'maxim'
if lower == stored:
    print(True)
else:
    print(False)


