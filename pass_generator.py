
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '|', '\\',
    ';', ':', "'", '"', ',',
    '.', '<', '>', '/', '?',
    '`', '~'
]

import random

password = ""

num_of_letters = int(input("enter the number of letters "))
num_of_symbols = int(input("enter the number of symbols "))
num_of_numbers = int(input("enter the number of numbers "))


for i in range(num_of_letters + 1):
    random_letter = random.choice(letters)
    password += random_letter
for i in range(num_of_symbols + 1):
    random_symbol = random.choice(symbols)
    password += random_symbol
for i in range(num_of_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number

list_password = list(password)
random.shuffle(list_password)
shuffle_pass = "".join(list_password)
print(shuffle_pass)
