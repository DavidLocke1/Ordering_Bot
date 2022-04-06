#from tabulate import tabulate

from tkinter import N


menu_items = ("Burger Budgie Special","Cheese Burger","Vegetarian Burger","Big Budgie Burger","Itsy-bitsy Burger",
              "Spiced chicken burger","Bacon-beef burger","Mega beef stacker burger","Beef stacker burger",
              "Seafood supreme burger","BBQ Eternal burger","Supreme stacker burger")
menu_prices = (6,4.5,4.5,5,3,5,5,6,5,5,5,6)
order_items = []
order_prices = []

def menu():
    table = []
    count = 0
    while count in range(len(menu_items)):
        table.append([count+1,menu_items[count],menu_prices[count]])
        count = count + 1

    for row in table:
        print("{: >5} {: <30} ${: <6.2f}".format(*row))
menu()
def ordering():
    while True:
        try:
            order_count = int(input("How many burgers would you like to order? "))
            if order_count == 0:
                print("Cannot order 0 Burgers")
            else:
                break
        except ValueError:
            print("This cannot be blank and must be a number")
    for item in range(order_count):
        while order_count > 0:
            print("Please enter a number between 1 and 12 for ordering")
            while True:
                try:
                    order = int(input("please enter a number from the menu to order your food "))
                    if order >= 1 and order <= len(menu_items):
                        order = order - 1
                        order_count = order_count - 1
                        order_items.append(menu_items[order])
                        order_prices.append(menu_prices[order])
                        print("{} ${:.2f}".format(menu_items[order], menu_prices[order]))
                        break
                    else:
                        print("Input must be a number from the menu")
                except ValueError:
                    print("Input must be a number and cannot be blank")
    

ordering()
