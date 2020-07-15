import numpy as np

def money_gamble():
    play_bool = input("Welcome to the Money Game. Do you want to play?")

    if play_bool.lower() in ["yes", "true", "y", "ja"]:
        number = input("So, you decided to play. That's great. we love playing at the pythonic Zoo. Let me quickly explain the rules: \n \
                        1. You will guess a number between 1 and 10. \n \
                        2. I will tell you the correct number.  \n \
                        3. If you guessed correctly, you will earn 100€. For every number you are off you get 25€ less. If you are more than 4 numbers off you have to pay 25 €.")
                        
        number = input("Please enter now your number:  ")
        number = int(number)
        random_number = np.random.randint(1, 11)
        print("The number was: {}".format(random_number))
        diff = abs(random_number - number)

        if diff > 4:
            print("Damn! You lost 25€.")
            return -25
        else:
            print("Congratulations! You won {} €.".format(100-(diff*25)))
            return 100-(diff*25)

    else:
        print("Lame!!!")
        return None


def sneak_in():
    pass