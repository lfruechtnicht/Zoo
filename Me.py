from ascii_me import beer


class Me(object):
    """ """

    def __init__(self, *, animals=['Monkeys', 'Lions'], money=None):
        """

        :param animals:
        :param money:
        """
        self.money = 0 if money is None else money
        self.food_bag = {"Bananas": 5}
        self.beers = 2
        self.location = "Shop"
        self.park_location = 0
        self.animals = animals
        self.alcohol_level = 0

    def __str__(self):
        return 'Morten'

    def change_location(self):
        """Change the location of Me to one of 'Entrance', 'Shop', 'Park'."""
        response = input("Would you like to go to the Entrance, the Shop or the Park?")
        while response not in ['Entrance', 'Shop', 'Park']:
            response = input("Please enter on of 'Entrance', 'Shop' or 'Park':")
        print(f'leaving to the {response}..')
        self.location = response

    def drink_beer(self, number_of_beers=1):
        """Drink a beer."""
        self.beers -= number_of_beers
        if self.beers < 0:
            print("Ops, you ran out of beers, quick go to the shop!")
            self.beers += number_of_beers
        else:
            self.alcohol_level += 0.3*number_of_beers
            for _beer in range(number_of_beers):
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

    def _view_animal(self):
        """view the representation of the animal inplace"""
        print(repr(self.animals[self.park_location]))

    def view_animal(self):
        """view the representation of the animal inplace"""
        self._view_animal()

    def walk_park(self):
        """Walk to the next animal in the park."""
        response = input("Do you want to see the next animal in the Zoo or go back to the previous?")
        while response not in ['next', 'previous']:
            response = input(f"Please enter 'next' or 'previous':")
        if response == 'next':
            try:
                self.park_location += 1
                print(f"You´ve arrived at the {self.animals[self.park_location]}.")
                print("\n\n")
                self._view_animal()
            except IndexError:
                self.park_location -= 1
                print("done")
        else:
            try:
                self.park_location -= 1
                print(f"You went back to the {self.animals[self.park_location]}.")
                print("\n\n")
                self._view_animal()
            except IndexError:
                print("done")
                self.park_location += 1

    def how_much_money_do_I_have(self):
        """:returns how much money you have."""
        print(self.money)

    def buy_beers(self):
        if self.location == "Shop":
            response = input("How many beers do you want to buy?")
            while response not in ["1","2","3","4","5","6","7","8","9",'all of them']:
                response = input("Please specify the number of beers")
            if response == 'all of them':
                # little cheat
                self.beers += 10
            else:
                money = self.money - int(response)
                if money >= 0:
                    self.beers += int(response)
                    self.money = money
                else:
                    print("You idiot don't have enough money for that many beers!")
        else:
            print('Your are not at the Shop and the monkey might pee on you but you can\' find beer here.')







if __name__ == '__main__':
    me = Me()
    me.drink_beer(2)
    me.buy_beers()

