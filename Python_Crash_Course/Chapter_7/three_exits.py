prompt = ''

while prompt != 'quit':
    prompt = int(input(
        'Enter your age to determine ticket price.\nType "quit" to end this program: '))
    if prompt < 3:
        print('The ticket is free\n')
    elif (prompt >= 3) and (prompt < 12):
        print('The ticket will be 10\n')
    elif prompt >= 12:
        print('The ticket will be 15$\n')

# -----------------------------------------------------------------------------

prompt = ''
active = True

while active:
    prompt = int(input(
        'Enter your age to determine ticket price.\nType "quit" to end this program: '))
    if prompt < 3:
        print('The ticket is free\n')
    elif (prompt >= 3) and (prompt < 12):
        print('The ticket will be 10\n')
    elif prompt >= 12:
        print('The ticket will be 15$\n')
    elif prompt == 'quit':
        print('Goodbye!')
        active = False

# ----------------------------------------------------------------------------

prompt = ''

while True:
    prompt = int(input(
        'Enter your age to determine ticket price.\nType "quit" to end this program: '))
    if prompt < 3:
        print('The ticket is free\n')
    elif (prompt >= 3) and (prompt < 12):
        print('The ticket will be 10\n')
    elif prompt >= 12:
        print('The ticket will be 15$\n')
    elif prompt == 'quit':
        print('Goodbye!')
        break
