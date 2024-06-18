class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f'The summary of {self.first_name.title()}\'s info:')
        print(f'\t{self.first_name}')
        print(f'\t{self.last_name}')
        print(f'\t{self.age}')
        print(f'\t{self.location}')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()}')


user1 = User('indra', 'kenz', '81', 'jail')
user1.describe_user()
user1.greet_user()

user2 = User('doni', 'salmanan', '29', 'jail')
user2.describe_user()
user2.greet_user()

user3 = User('charles', 'stevano', '24', 'ohio')
user3.describe_user()
user3.greet_user()
