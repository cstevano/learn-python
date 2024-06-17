def make_album(artist, album, number_of_songs=None):
    person = {'artist': artist, 'album': album}
    if number_of_songs:
        person['number_of_songs': number_of_songs]
    return person


print(make_album('Post Malone', 'Congratulations'))
print(make_album('Aimer', 'Noir'))
print(make_album('boy pablo', 'Wachito Rico'))
