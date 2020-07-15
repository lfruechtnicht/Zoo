import numpy as np
import time

def money_gamble():
    """
        Parameters
        ----------
        
        Returns
        -------
        amount of money or None
    """
    play_bool = input("Welcome to the Money Game. Do you want to play?")

    if play_bool.lower() in ["yes", "true", "y", "ja"]:
        print("So, you decided to play. That's great. we love playing at the pythonic Zoo. Let me quickly explain the rules:")
        input("1. You will guess a number between 1 and 10.")
        input("2. I will tell you the correct number.")
        input("3. If you guessed correctly, you will earn 100€. For every number you are off you get 25€ less. If you are more than 4 numbers off you have to pay 25 €.")                 
        
        number = int(input("Please enter now your number:  "))

        random_number = np.random.randint(1, 11)
        print("The number was: {}".format(random_number))
        
        diff = abs(random_number - number)

        if diff > 4:
            print("Damn! You lost 25€.")
            return -25
        elif diff == 4:
            print("Thank god. That was even stevens!")
            response = input("Do you want to try again?")
            if response.lower() in ["yes", "y", "ja"]:
                return money_gamble()
            else:
                return 0
        else:
            print("Congratulations! You won {} €.".format(100-(diff*25)))
            return 100-(diff*25)

    else:
        print("Lame!!!")
        return 0


def sneak_in():
    input(
    "So, you want to jump the fence. Sneaky!!! \n \
    The deal is the following: In exactly 20 seconds from now there's a guard change. It takes 5 seconds. \n \
    If you manage to sneak into the Zoo during this timeframe you don't get busted. \n \
    The time starts after you it enter.")
    start = time.time()
    response = input()
    end = time.time()
    delta = int(end - start)

    print("You tried to sneak in after {} seconds.".format(delta, 0))

    if delta in range(20, 26):
        print("You managed to sneak in.")
    
    else:
        print("BUSTED!!! You got caught by the guard. You are not going to the Zoo today.")

    