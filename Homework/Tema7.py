# task 1
def string(word):
    word = word.replace(",", "").replace(".", "")
    words = word.split()

    # Count the occurrences of each word
    dictionar = {}
    for word in words:
        if word in dictionar:
            dictionar[word] += 1
        else:
            dictionar[word] = 1

    return dictionar
user_word = input("Enter a string: ")
result = string(user_word)
print(result)

# task 2
def calcul_total(stock, prices):
    total_price = 0

    for item in stock:
        if item in prices:
            total_price += stock[item] * prices[item]
    
    return total_price

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = calcul_total(stock, prices)
print(f"The total price of the stock is: ${total_price}")

# task 3
result = [(i, i ** 2) for i in range(1, 11)]
print(result)
