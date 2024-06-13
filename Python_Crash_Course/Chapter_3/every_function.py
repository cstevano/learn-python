train_station = ['Bogor', 'Depok', 'Cilebut', 'Bojong Gede', 'Citayam']

inactive_train_station = train_station.pop()
train_station.remove('Bogor')
train_station.append('Pondok Cina')
train_station.insert(0, 'Lenteng Agung')
train_station.sort()
train_station.sort(reverse=True)
del train_station[1]
print(sorted(train_station))
print(sorted(train_station, reverse=True))
train_station.reverse()
train_station.reverse()
print(f'The length of the list are: {len(train_station)}')

