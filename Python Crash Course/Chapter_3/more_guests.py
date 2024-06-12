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
invite_list.append('Holan\n')

print(f'Hi {invite_list[0]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[1]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[2]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[3]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[4]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[5]}, you are invited to join at my party tonight!')
print(f'Hi {invite_list[6]}, you are invited to join at my party tonight!\n')