import random

x = random.randint(1, 100) 
y = int(input("Zadej hodnotu y "))

  
def sudy_lichy(num_1):
    if (num_1 % 2) == 0:
        return "{0} je sudé".format(num_1)
    else:
        return "{0} je liché".format(num_1)

print(sudy_lichy(x))
print(sudy_lichy(y))
