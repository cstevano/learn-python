class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The restaurant name is {self.restaurant_name}')
        print(f'The restaurant type is {self.cuisine_type}\n')

    def open_restaurant(self):
        print('The restaurant is now open')


restaurant1 = Restaurant('Loong', 'Chinese food')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('Jollibee', 'Philippines food')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Haidilao', 'Buffet')
restaurant3.describe_restaurant()
