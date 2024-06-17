def city_country(city, country):
    citycountry = f'{city.title()}, {country.title()}'
    return citycountry


print(city_country('Bogor', 'Indonesia'))
print(city_country('Bangkok', 'Thailand'))
print(city_country('Mumbai', 'India'))
