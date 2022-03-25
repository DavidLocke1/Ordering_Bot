import random
from random import randint
from tkinter import N
from operator import truediv

# dictionaries and lists
user_details = {}

names = ["Mark", "Pheobe", "Sally", "Michael", "Denise",
         "Ellen", "Eris", "Moana", "Lewis", "Lara"]

# functions
def not_valid_alphaonly(question):
    valid = False
    while not valid:
        print("")
        answer = input(question)
        if answer != "" and any(x.isnumeric() for x in answer) == False:
            return answer.title()
        elif answer != "":
            print("Answer must not include numbers")
        else:
            print("Sorry this cannot be blank")

def not_valid_numonly(question):
    valid = False
    while not valid:
        print("")
        answer = input(question)
        if answer != "" and answer.isnumeric():
            return answer.title()
        elif answer != "":
            print("Answer must not include letters or spaces")
        else:
            print("Sorry this cannot be blank")
        
def not_valid(question):
    valid = False
    while not valid:
        print("")
        answer = input(question)
        if answer != "":
            return answer.title()
        else:
            print("Sorry this cannot be blank")

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
                pickup_request()
                break
            elif delivery_option == 2:
                print("Delivery")
                delivery_request()
                break
            else:
                print("Please choose pickup or delivery")
                print("To choose")
                order_message()
        except ValueError:
            print("You must choose pickup or delivery by typing 1 or 2")
            order_message()

# pickup function
def pickup_request():
    question = ("Please enter your name ")
    user_details['name'] = not_valid_alphaonly(question)
    print(user_details['name'])

    question = ("Please enter your phone number ")
    user_details['phonenumber'] = not_valid_numonly(question)
    print(user_details['phonenumber'])

    print("")
    print(user_details['name'])
    print(user_details['phonenumber'])

# Delivery function
def delivery_request():
    question = ("Please enter your name ")
    user_details['name'] = not_valid_alphaonly(question)
    print(user_details['name'])

    question = ("Please enter your phone number ")
    user_details['phonenumber'] = not_valid_numonly(question)
    print(user_details['phonenumber'])

    question = ("What is your house number? ")
    user_details['housenumber'] = not_valid(question)
    print(user_details['housenumber'])

    question = ("Please enter your street name ")
    user_details['streetname'] = not_valid_alphaonly(question)
    print(user_details['streetname'])

    question = ("Please enter your suburb ")
    user_details['suburb'] = not_valid_alphaonly(question)
    print(user_details['suburb'])

    print("")
    print(user_details['name'])
    print(user_details['phonenumber'])
    print(user_details['housenumber'])
    print(user_details['streetname'])
    print(user_details['suburb'])

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