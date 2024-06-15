sandwich_orders = ['fruit sandwich', 'beef sandwich', 'chicken sandwich',
                   'vegan sandwich', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print('The Deli has ran out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_in_progress = sandwich_orders.pop()
    print(f'Making sandwich: {sandwich_in_progress.title()}')
    print(f'Finished making {sandwich_in_progress.title()}\n')
    finished_sandwiches.append(sandwich_in_progress)
