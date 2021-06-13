dict = {}
# cards = []
cards = str(int(input()))
new_cards = cards.replace('6', '9')
print(new_cards)
new_cards = list(new_cards)
print(new_cards)

for i in range(len(new_cards)):
    if new_cards[i] not in dict.keys():
        dict[new_cards[i]] = 1
    else:
        dict[new_cards[i]] += 1

print(dict)
print(max(dict.values()))
print(dict.values())


# dict = {}
#
# dict['sewon'] = 4
#
# if 'sewon' in dict.keys():
#     print('yay')
#     dict['sewon'] -= 1
#
#     print(dict)

