import random
from random import randint
from tkinter import N
from operator import truediv

names = ["Mark", "Pheobe", "Sally", "Michael", "Denise",
         "Ellen", "Eris", "Moana", "Lewis", "Lara"]

# welcome message- choosesn random name and prints welcome message using that name
def welcome_message():
    num = randint(0,len(names)-1)
    name = (names[num])
    print("* * * * * * * *")
    print(" *")
    print("* *  Welcome to Budgie's burger's")
    print(" *   My name is ", name)
    print("* *  I am here to take your order")
    print(" *")
    print("* * * * * * * *")
    print("")

# Order tupre- asks the user to choose pickup or delivery and validats input to make sure it is correct
def order_type():
    def order_message():
        print("Type 1 for pickup")
        print("Type 2 for delivery")
    print("Would you like your order for pickup or delivery")
    order_message()
    while True:
        try:
            delivery_option = int(input())
            if delivery_option == 1:
                print("Pickup")
                break
            elif delivery_option == 2:
                print("Delivery")
                break
            else:
                print("Please choose pickup or delivery")
                print("To choose")
                order_message()
        except ValueError:
            print("You must choose pickup or delivery by typing 1 or 2")
            order_message()

# pickup function

# Delivery function

# menu function

# ordering function

# reciet function

# Confirm or cancel function

# new order or exit function

# main function
def main():
    welcome_message()
    order_type()

# Running program
main()