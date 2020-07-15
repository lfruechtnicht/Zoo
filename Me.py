from ascii_me import beer


class Me(object):


    def __init__(self, money=None):
        self.money = 0 if money is None else money
        self.food_bag = {"Bananas": 5}
        self.beers = 0
        self.location = "Entrance"
        self.park_location = 0
        self.animals = ['Monkeys']

    def change_location(self):
        """Change the location of Me to one of ['Entrance', 'Shop', 'Park']"""
        response = input("Would you like to go to the Entrance, the Shop or the Park?")
        while response not in ['Entrance', 'Shop', 'Park']:
            response = input("Please enter on of 'Entrance', 'Shop' or 'Park':")
        print(f'leaving to the {response}..')
        self.location = response

    def drink_beer(self):
        """Drink a beer."""
        self.beers -= 1
        if self.beers < 0:
            print("Ooops you ran out of beers, quick go to the shop!")
            self.beers = 0
        else:
            print(beer)

    def feed(self):
        """Feed one food item from the food"""
        if not self.food_bag or sum(self.food_bag.values()) == 0:
            # if the foodbag is empty:
            print('You ran out of food! Go back to the shop to buy new animal food')
        else:
            response = input(f'What would you like to feed the {self.animals[self.park_location]}? You currently have: {self.food_bag}')
            while response not in self.food_bag.keys():
                response = input(f"Please enter one of {self.food_bag.keys()}:")




if __name__ == '__main__':
    me = Me()
    me.feed()