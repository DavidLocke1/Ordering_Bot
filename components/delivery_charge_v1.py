#from tabulate import tabulate

from tkinter import N


menu_items = ("Burger Budgie Special","Cheese Burger","Vegetarian Burger","Big Budgie Burger","Itsy-bitsy Burger",
              "Spiced chicken burger","Bacon-beef burger","Mega beef stacker burger","Beef stacker burger",
              "Seafood supreme burger","BBQ Eternal burger","Supreme stacker burger")
menu_prices = (6,4.5,4.5,5,3,5,5,6,5,5,5,6)
order_items = []
order_prices = []
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
                delivery_type = "pickup"
                break
            elif delivery_option == 2:
                print("Delivery")
                delivery_type = "delivery"
                break
            else:
                print("Please choose pickup or delivery")
                print("To choose")
                order_message()
        except ValueError:
            print("You must choose pickup or delivery by typing 1 or 2")
            order_message()
order_type()
def menu():
    table = []
    count = 0
    #menu_max_length = 0
    while count in range(len(menu_items)):
        table.append([count+1,menu_items[count],menu_prices[count]])
        #item_length = len(menu_items[count])
        #if item_length > menu_max_length:
        #    menu_max_length = item_length
        count = count + 1

    for row in table:
        print("{: >5} {: <30} ${: <6.2f}".format(*row))
menu()
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
    

ordering()

def deliverycharge():
    if order_amount < 5 and delivery_type == "delivery":
        order_items.append("Delivery Charge")
        order_prices.append(9)
    elif delivery_type == "delivery":
        order_items.append("Delivery Charge")
        order_prices.append(0)


deliverycharge()

print(order_items)
