current_users = ['Admin', 'Johndoe', 'Atomic', 'Foobar', 'Helloworld']
lowcase_current_users = [user.lower() for user in current_users]
new_users = ['johndoe', 'diana', 'atomic', 'kanye', 'west']

for new_user in new_users:
    if new_user in lowcase_current_users:
        print('You will need to enter a new username')
    else:
        print('This username is available.')
