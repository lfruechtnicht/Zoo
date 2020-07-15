from utils import money_gamble, sneak_in
from animal import Animal
from animal_ascii import lion

print("WELCOME TO THE PYTHONIC ZOO!")
print("You have no money right now. You could either try to gamble to get money or you try to sneak in.")

response = input("What do you want to do?")

while response.lower() not in ["gamble", "get money", "sneak in", "sneak"]:
    response = input("I don't understand. Please repeat: ")

if response in ["gamble", "get money"]:
    money = money_gamble()

elif response in ["sneak in", "sneak"]:
    print("Very brave!")
    sneak_in()

