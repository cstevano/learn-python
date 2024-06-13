invite_list = ['Doni', 'Salmanan', 'Indra', 'Kenz']

print(f'Hi {invite_list[0]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[1]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[2]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[3]}, you are invited to join at my party tonight!')

print("\n" + invite_list[3] + " can't make it to the party\n")
invite_list[3] = 'Timothy'

print(f'Hi {invite_list[0]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[1]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[2]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[3]}, you are invited to join at my party tonight!')

print("\nErm guys, there's actually a bigger table in the marketplace! i think we could invite more people to join us tonight.\n")

invite_list.insert(0, 'Denis')
invite_list.insert(2, 'Jarwo')
invite_list.append('Holan')

print(f'Hi {invite_list[0]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[1]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[2]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[3]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[4]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[5]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[6]}, you are invited to join at my party tonight!\n')

print("Ackshually, it turns out that the dinner table is only for 2 people. so, we can only invite 2 people to join us\n")

x = invite_list.pop()
print(f'Hi {x}, i am sorry to inform you that the table is only fit for 2 people')

x = invite_list.pop()
print(f'Hi {x}, i am sorry to inform you that the table is only fit for 2 people')

x = invite_list.pop()
print(f'Hi {x}, i am sorry to inform you that the table is only fit for 2 people')

x = invite_list.pop()
print(f'Hi {x}, i am sorry to inform you that the table is only fit for 2 people')

x = invite_list.pop()
print(f'Hi {x}, i am sorry to inform you that the table is only fit for 2 people')

print(f'\nHi {invite_list[0]}, I would like to inform you that while the table only fit for 2 people, you are still invited. I hope you can join me tonight!')

print(f'\nHi {invite_list[1]}, I would like to inform you that while the table only fit for 2 people, you are still invited. I hope you can join me tonight!')

del invite_list[1]
del invite_list[0]

print(f'\nInvited guest: {invite_list}')


