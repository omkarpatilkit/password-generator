import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
l = []
n = []
s = []

for i in range(nr_letters):
    a = random.randint(0, len(letters)-1)
    l.append(letters[a])
print(l)

for i in range(nr_numbers):
    a = random.randint(0, len(numbers)-1)
    n.append(numbers[a])
print(n)

for i in range(nr_symbols):
    a = random.randint(0, len(symbols)-1)
    s.append(symbols[a])
print(s)

final = l+s+n
pswd = ''

set_final = set(final)
print(set_final)
for i in set_final:
    pswd = pswd+i

print(pswd)
