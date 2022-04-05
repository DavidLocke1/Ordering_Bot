import random
from random import randint
from tkinter import N
from operator import truediv

# dictionaries and lists
user_details = {}

names = ["Mark", "Pheobe", "Sally", "Michael", "Denise",
         "Ellen", "Eris", "Moana", "Lewis", "Lara"]

menu_items = ("Burger Budgie Special","Cheese Burger","Vegetarian Burger","Big Budgie Burger","Itsy-bitsy Burger",
              "Spiced chicken burger","Bacon-beef burger","Mega beef stacker burger","Beef stacker burger",
              "Seafood supreme burger","BBQ Eternal burger","Supreme stacker burger")
menu_prices = (6,4.5,4.5,5,3,5,5,6,5,5,5,6)
order_items = []
order_prices = []

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

def phone_check(question,phone_low,phone_high):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= phone_low and count <= phone_high:
                return str(num)
            else:
                print("Phone numbers have between 7 and 10 digits")
        except ValueError:
            print("Please enter a number")
        
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
    global delivery_type
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
                delivery_type = "pickup"
                break
            elif delivery_option == 2:
                print("Delivery")
                delivery_request()
                delivery_type = "delvivery"
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
    phone_low = 7
    phone_high = 10
    user_details['phonenumber'] = phone_check(question,phone_low,phone_high)
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
    phone_low = 7
    phone_high = 10
    user_details['phonenumber'] = phone_check(question,phone_low,phone_high)
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
def menu():
    table = []
    count = 0
    while count in range(len(menu_items)):
        table.append([count+1,menu_items[count],menu_prices[count]])
        count = count + 1

    for row in table:
        print("{: >5} {: <30} ${: <6.2f}".format(*row))

# ordering function
def ordering():
    global order_amount
    while True:
        try:
            order_count = int(input("How many burgers would you like to order? "))
            order_amount = order_count
            break
        except ValueError:
            print("This cannot be blank and must be a number")
    for item in range(order_count):
        while order_count > 0:
            print("PLease enter a number between 1 and 12 for ordering")
            while True:
                try:
                    order = int(input("please enter a number from the menu to order your food "))
                    if order >= 1 and order <= len(menu_items) + 1:
                        break
                    else:
                        print("Input must be a number from the menu")
                except ValueError:
                    print("Input must be a number and cannot be blank")
            order = order - 1
            order_count = order_count - 1
            order_items.append(menu_items[order])
            order_prices.append(menu_prices[order])
            print("{} ${:.2f}".format(menu_items[order], menu_prices[order]))

# calculating delivery charge
def deliverycharge():
    if order_amount <= 5 and delivery_type == "delivery":
        order_items.append("Delivery Charge")
        order_prices.append(9)
    elif delivery_type == "delivery":
        order_items.append("Delivery Charge")
        order_prices.append(0)
# reciet function

# Confirm or cancel function

# new order or exit function

# main function
def main():
    welcome_message()
    order_type()
    menu()
    ordering()
    deliverycharge()

# Running program
main()