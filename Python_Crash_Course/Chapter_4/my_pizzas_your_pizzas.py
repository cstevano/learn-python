my_pizzas = ['pepperoni', 'pineapple', 'cheese']
friend_pizzas = my_pizzas[:]

my_pizzas.append('neapolitan')
friend_pizzas.append('meat lovers')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print()

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)