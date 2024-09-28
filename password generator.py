import random
import string
print("Welcome to Password Generator!")
r=int(input("Please select how many letters included in string"))
letters=string.ascii_letters

digits=['0','1','2','3','4','5','6','7','8','9']
symbols = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/']


h=int(input("How many numbers do you wnat in your password"))
u=int(input("How many letters do you wnat in your password"))
e=int(input("How many symbols do you wnat in your password"))
y=[]
for i in range(0,h):
    y.append(random.choice(digits))
for i in range(0,u):
    y.append(random.choice(letters))
for i in range(0,e):
    y.append(random.choice(symbols))

random.shuffle(y)
print("".join(i for i in y))

