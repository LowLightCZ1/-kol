import random

x = random.randint(1, 50) 
y = int(input("Zadej hodnotu y "))


while y != x:
    if x > y:
        print("Myslím si větší")  
    
    else:
        print("Myslím si menší")
    y = int(input("Zadej hodnotu y "))
print("Uhádl jsi :) ")