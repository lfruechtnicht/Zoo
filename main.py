from utils import money_gamble, sneak_in
from animal import Animal
from animal_ascii import lion

print("WELCOME TO THE PYTHONIC ZOO!")
input()
print("You have no money right now. You could either try to gamble to get money or you try to sneak in.")
input()

response = input("What do you want to do? ")

while response.lower() not in ["gamble", "get money", "sneak in", "sneak", "play"]:
    response = input("I don't understand. Please repeat: ")

if response.lower() in ["gamble", "get money", "play"]:
    money = money_gamble()

elif response.lower() in ["sneak in", "sneak"]:
    sneak_in()

