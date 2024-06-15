cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 13_960_000,
        'fact': 'Tokyo Disneyland is the first Disneyland that built outside US',
    },

    'Bogor': {
        'country': 'Indonesia',
        'population': 820_707,
        'fact': 'Has a delicious food called "Soto Mie"',
    },

    'Depok': {
        'country': 'Indonesia',
        'population': 2_484_000,
        'fact': 'A lot of things happened here....'
    },
}

for city, info in cities.items():
    print(f'\n{city} details:')
    for details, description in info.items():
        print(f'\t{details}: {description}')
