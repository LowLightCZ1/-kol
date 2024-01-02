def card_hide(card_num):
    return card_num[:4] + (len(card_num) - 4) * "*"
   
print(card_hide("132568834900123468"))