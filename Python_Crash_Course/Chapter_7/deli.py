sandwich_orders = ['fruit sandwich', 'beef sandwich', 'chicken sandwich',
                   'vegan sandwich']

finished_sandwiches = []

while sandwich_orders:
    sandwich_in_progress = sandwich_orders.pop()
    print(f'Making sandwich: {sandwich_in_progress.title()}')

    print(f'Finished making {sandwich_in_progress.title()}\n')
    finished_sandwiches.append(sandwich_in_progress)
