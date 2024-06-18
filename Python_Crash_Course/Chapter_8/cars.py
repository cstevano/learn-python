def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = make_car('Honda', 'City', year='2014', color='black')
print(car)
