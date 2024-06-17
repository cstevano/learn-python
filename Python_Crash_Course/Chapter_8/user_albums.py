def make_album(artist, album):
    person = {'artist': artist, 'album': album}
    return person


while True:
    print('\nWelcome to Make Album program, please enter "q" anytime to quit')
    artist = input('Please enter the name of the artist: ')
    if artist == 'q':
        break

    album = input('Please enter the name of the album: ')
    if album == 'q':
        break

    new_album = make_album(artist, album)
    print(new_album)
