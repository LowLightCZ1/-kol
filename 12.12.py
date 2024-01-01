#def list_swap(list, old_num, new_num):
    #for i in range (len(list)):
    #    if list[i] == old_num:
     #       list[i] = new_num
    #return list

#print(list_swap([1, 10, 5, 6, 7, 5, 45], 5, 0))



#def is_last_char_k(name):
   # if name[-1] == "k":
   #     return True
   # else:
   #     return False
    
#print (is_last_char_k("Jakub"))


#def card_hide(card_num):
    # return 12 * "*" + card_num[12:]
   # hiden_card = []
   # for i in range(len(card_num)):
       # if i < 12:
        #    hiden_card.append("*")
       # else:
       #     hiden_card.append(card_num[i])
   # return "".join
   
#print(card_hide("132568834900123468"))


x = int(input("zadej váhu"))
y = int(input("zadej výšku"))
    
bmi = x / ((y/100)* (y/100))

if bmi < 19:
    print("Máš podváhu")
elif bmi <= 25:
    print("Mormální váha")
else: 
    print("Máš nadváhu")
    

    
    
        
    