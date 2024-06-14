foods = ('aglio olio', 'foie gras', 'carbonara', 'pizza', 'fried rice')

print('Our restaurant menu:')
for food in foods:
    print(food)

# the code below is an invalid code because tuple is immutable
# foods[0] = 'satay' 

# changing the tuple's value by re-writing the whole tuple

foods = ('satay', 'fried chicken', 'carbonara', 'pizza', 'fried rice')

print('\nOur new menu:')
for food in foods:
    print(food)
