def card_hide(card_numb):
    return 12 * "*" + card_numb[12:]
hiden_card = []
for i in range(len(card_num)):
    if i < 12:
        hiden_card.append("*")
    else:
        hiden_card.append(card_num[i])
return "".join

print(card_hide("132568834900123468"))
