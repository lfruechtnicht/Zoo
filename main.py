from utils import money_gamble, sneak_in, response_function, entrance
from Me import Me
from animal import Animal
from animal_ascii import lion

print("WELCOME TO THE PYTHONIC ZOO!")
input()
input("You have no money right now. You could either try to gamble to get money or you try to sneak in.")

me = Me()

response = input("What do you want to do? ")

while response.lower() not in ["gamble", "get money", "sneak in", "sneak", "play", "money"]:
    response = input("I don't understand. Please repeat: ")

if response.lower() in ["gamble", "get money", "play", "money"]:
    money = money_gamble()

elif response.lower() in ["sneak in", "sneak"]:
    if sneak_in():
        me.location = 'Park'

if me.location == "Entrance":
    money = entrance(money)
    me.money = money

input("Congratulations! You are in the Zoo.")