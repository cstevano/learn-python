message = ''

while message != 'quit':
    message = input(
        'Please enter the topping you would like to add.\nType "quit" if you want to exit:  ')
    if message != 'quit':
        print(f'Sure, i will add {message} to your pizza.\n')
