def sandwich_contents(*contents):
    print('The content of the sandwich are:')
    for content in contents:
        print(f'\t{content}')


sandwich_contents('pepperoni', 'cucumber', 'beef')
sandwich_contents('cheese')
sandwich_contents('chicken teriyaki', 'tomato')
