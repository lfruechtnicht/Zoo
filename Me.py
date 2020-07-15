from ascii_me import beer


class Me(object):

    def __init__(self, *, animals=['Monkeys', 'Lions'], money=None):
        self.money = 0 if money is None else money
        self.food_bag = {"Bananas": 5}
        self.beers = 0
        self.location = "Entrance"
        self.park_location = 0
        self.animals = animals

    def change_location(self):
        """Change the location of Me to one of 'Entrance', 'Shop', 'Park'."""
        response = input("Would you like to go to the Entrance, the Shop or the Park?")
        while response not in ['Entrance', 'Shop', 'Park']:
            response = input("Please enter on of 'Entrance', 'Shop' or 'Park':")
        print(f'leaving to the {response}..')
        self.location = response

    def drink_beer(self):
        """Drink a beer."""
        self.beers -= 1
        if self.beers < 0:
            print("Ooops, you ran out of beers, quick go to the shop!")
            self.beers = 0
        else:
            print(beer)

    def feed(self):
        """Feed one food item from the food."""
        if not self.food_bag or sum(self.food_bag.values()) == 0:
            # if the food_bag is empty:
            print('You ran out of food! Go back to the shop to buy new animal food')
        else:
            response = input(f'What would you like to feed the {self.animals[self.park_location]}? You currently have: '
                             f'{self.food_bag}')
            while response not in self.food_bag.keys():
                response = input(f"Please enter one of {self.food_bag.keys()}:")
            print(f"Fed the {self.animals[self.park_location]}  with {response}.")

    def view_animal(self):
        pass

    def walk_park(self):
        """Walk to the next animal in the park."""
        response = input("Do you want to see the next animal in the Zoo or go back to the previous?")
        while response not in ['next', 'previous']:
            response = input(f"Please enter 'next' or 'previous':")
        if response == 'next':
            try:
                self.park_location += 1
                print(f"You´ve arrived at the {self.animals[self.park_location]}.")
            except IndexError:
                self.park_location -= 1
                print("done")
        else:
            try:
                self.park_location += 1
                print(f"You went back to the {self.animals[self.park_location]}.")
            except IndexError:
                print("done")
                self.park_location += 1




if __name__ == '__main__':
    me = Me()
    me.walk_park()
    me.walk_park()
