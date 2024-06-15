favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

should_take_poll = ['jen', 'phil', 'indra', 'doni']

for name in should_take_poll:
    if name in favorite_languages:
        print(f'Hi {name.title()}, Thanks for polling.')
    elif name not in favorite_languages:
        print(f'Hi {name.title()}, Please poll!!!!!!')
