# using code from 4-6 programs
odd_numbers = list(range(1, 21, 2))

print('The first three items in the list are:')
for number in odd_numbers[:3]:
    print(number)
print()

print('Three items from the middle of the list are:')
for number in odd_numbers[5:8]:
    print(number)
print()

print('The last three items in the list are:')
for number in odd_numbers[-3:]:
    print(number)