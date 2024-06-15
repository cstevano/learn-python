favorite_numbers = {
    'Charles': [90, 25],
    'Doni': [21, 78],
    'Salmanan': [12, 35],
    'Indra': [301, 120],
}

for name, numbers in favorite_numbers.items():
    print(f'\n{name}\'s favorite numbers are:')
    for number in numbers:
        print(number)
