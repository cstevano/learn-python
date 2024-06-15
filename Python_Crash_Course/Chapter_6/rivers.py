rivers = {
    'nile': 'egypt',
    'mekong': 'china',
    'yangtze': 'china',
}

for river, location in rivers.items():
    print(f'The {river} runs through {location}')

for river in rivers:
    print(river)

for location in rivers.values():
    print(location)
