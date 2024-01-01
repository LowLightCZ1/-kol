x = int(input("zadej váhu"))
y = int(input("zadej výšku"))
    
bmi = x / ((y/100)* (y/100))

if bmi < 19:
    print("Máš podváhu")
elif bmi <= 25:
    print("Mormální váha")
else: 
    print("Máš nadváhu")
