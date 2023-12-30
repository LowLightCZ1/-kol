import random

x = random.randint(1, 10)
y = int(input("Zadej hodnotu y "))

if x == y:
    print("Uhádl jsi :)")
else:
    print("Neuhádl jsi :(")

