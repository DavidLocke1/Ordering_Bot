import random # Imports all needed exstensions
from random import randint
from tkinter import N
from operator import truediv
import sys

# Created all main dictionaries and lists for the program
user_details = {} # Creates main dictionary for the user details
# Creates the list of names and the menu lists
names = ["Mark", "Pheobe", "Sally", "Michael", "Denise",
         "Ellen", "Eris", "Moana", "Lewis", "Lara"]
menu_items = ("Burger Budgie Special","Cheese Burger","Vegetarian Burger","Big Budgie Burger","Itsy-bitsy Burger",
              "Spiced chicken burger","Bacon-beef burger","Mega beef stacker burger","Beef stacker burger",
              "Seafood supreme burger","BBQ Eternal burger","Supreme stacker burger")
menu_prices = (6,4.5,4.5,5,3,5,5,6,5,5,5,6)
# Creates the two list for what the user orders
order_items = []
order_prices = []

# Validates input to mkae sure it is between a low and high
# Takes low high and question as paramaters
# Returns answer if valid entry
def while_true(low,high,question): # Creates function and brings in parameters low high and question
    while True: # Creates a loop which will continue to loop until told to stop
        try: # attempts to perform code inside
            answer = int(input(question)) # asks for input integer using parameter question
            if answer >= low and answer <= high: # checks if answer is between the low and high parameters
                return answer # returns the answer out of the function
            else: # runs if answer is not between low and high parameters
                print(f"Please enter a number between {low} and {high}")
        except ValueError: # will run if try recieves a valueerror and cannot complete
            print(f"You must choose by typing a number between {low} and {high}")

# Validates inputs to make sure they only contain letters
# Takes in question as parameter
# Returns answer in title class if it does not contain any numbers
def not_valid_alphaonly(question): # Created function and brings in parameter question
    valid = False # Sets valid to false for loop
    while not valid: # Sets up while loop
        print("") # Prints blank line
        answer = input(question) # Asks for input and makes answer variable using the parameter question
        if answer != "" and any(x.isnumeric() for x in answer) == False: # If statement , First part makes sure answer variable is not blank, secound part checks each individual character in the variable answer for any unwanted numbers. 
            return answer.title() # returns the answer variable if the "if" statement is true (no numbers and not blank)
        elif answer != "": # Prints error message if answer variable is not blank only (so it has atleast one number in the answer variable)
            print("Answer must not include numbers")
        else: # prints error message if "if" and "else if" parameters not met
            print("Sorry this cannot be blank")

# validates input to make sure it is only a valid phone number
# Takes in question, phone_low, and phone_high as parameters
# Returns answer if it is a valid phone number
def phone_check(question,phone_low,phone_high): # Creates function and brings in parameters "question", "phone_low", and "phone_high"
    print("") # Prints blank line
    while True: # Makes a while loop that will run until stopped by return      
        try: # Attempts to run following code 
            num = int(input(question)) # Asks question, checks that it is an integer and sets the variable num to the answer 
            test_num = num # Sets the variable test_num to be the same as num
            count = 0 # Creates the variable count and sets it to 0
            while test_num > 0: # Creates a while loop which will run while test_num is greater then 0 to count how many digits is in the answer 
                test_num = test_num//10 # Sets test_num to its own value divided by ten
                count = count + 1 # Adds one to the count variable
            if count >= phone_low and count <= phone_high: # Checks if the count is between phone low and phone high
                return str(num) # Returns the value of num (phone number) in the form of a string
            else: # Runs if the if statement doesn't
                print("Phone numbers have between 7 and 10 digits") # Prints error message about length of phone number
        except ValueError: # Prints error message if the try fails because of a value error
            print("Please enter a phone number without any spaces") # Prints error message about entering a number

# Validates input to make sure that it is not blank
# Takes in question as a parameter
# Returns answer in title class if it is not blank        
def not_valid(question): # creates not_valid function and brings in variable question
    valid = False # Makes the variable valid equal to False
    while not valid: # creates a while loop
        print("") # Prints a blank line
        answer = input(question) # Asks question and sets the variable answer to the input
        if answer != "": # If statement which runs if the answer is not blank
            return answer.title() # Returns the answer variable
        else: # Prints the error message if the if statement is not meet
            print("Sorry this cannot be blank") 

# Prints a message welcoming the user to Budgies Burger
# Welcome message is printed from a randomly generated name
def welcome_message(): # Creates the welcome message function
    num = randint(0,len(names)-1) # Sets the variable num to a randomly generated number between 0 and the total number of names in the names list (len)
    name = (names[num]) # Creates a variable named name and sets it to the name from the list using the random number
    print("\n\n\n\n\n\n\n\n\n\n") # prints ten lines
    print("* * * * * * * *") # prints welcome message
    print(" *")
    print("* *  Welcome to Budgie's burger's")
    print(" *   My name is ", name) # Prints randomly generated name
    print("* *  I am here to take your order")
    print(" *")
    print("* * * * * * * *")
    print("")

# Allows the user to choose if they want their order for delivery or pickup
# does not take any parameters
# Changes a global variable for which answer is choosen
def order_type(): # Creates a function named order_type()
    global delivery_type # Makes the variable delivery_type global so that it can be used by code outside of this function
    print("Would you like your order for pickup or delivery") # Prints intial question
    question = ("Type 1 for pickup \nType 2 for delivery\n") # Creates the variable question and makes it the question
    LOW = 1 # Creates the constant LOW with the number one
    HIGH = 2 # Creates the constant HIGh with the number two
    delivery_option = while_true(LOW,HIGH,question) # Gives the while true function LOW HIGH and question parameters and makes the variable delivery option the returned value
    if delivery_option == 1: # Checks if the delivery option variable is one
        print("Pickup") # Tells the user what they choose by printing Pickup
        pickup_request() # Runs the pickup request function
        delivery_type = "pickup" # Sets the global variable delivery type to pickup
    elif delivery_option == 2: # Checks if the delivery option variable is two
        print("Delivery") # Tells the user they picked delivery by printing Delivery
        delivery_request() # Runs the delivery request function
        delivery_type = "delivery" # Sets the global variable delivery type to delivery
    print("\n\n\n\n\n\n\n\n\n\n") # Prints ten blank lines

# Collects the users details (name, phonenumber)for if they choose pickup
# Does not take in any parameters
# Adds answers to a dictionary for later use
def pickup_request(): # Creates the function pickup_request
    question = ("Please enter your name ") # Makes the variable question the new question
    user_details['name'] = not_valid_alphaonly(question) # Gives the not_valid_alphaonly function the parameter question and adds the responce to the dictionary user_details under name
    print(user_details['name']) # Prints the name
    question = ("Please enter your phone number ") # Sets the question variable to the phone number question
    phone_low = 7 # Creates phone_low and makes it seven
    phone_high = 10 # Creates phone_high and makes it ten
    user_details['phonenumber'] = phone_check(question,phone_low,phone_high) # Gives the phone_check function the parameters question, phone_low, and phone_high and adds the responce to the dictionary user_details under phonenumber
    print(user_details['phonenumber']) # Prints the phone number
    print("") # Prints a blank line
    print(user_details['name']) # Prints nmae from dictionary again
    print(user_details['phonenumber']) # Prints phone number from dictionary again
    print("\n\n\n\n\n\n\n\n\n\n") # Prints 10 blank lines

# Collects the user details (nam, phonenumber, and address) for if they choose delivery
# Does not take in any parameters
# Adds answers to the dictionary for later use
def delivery_request(): # Creates the function delivery_request
    question = ("Please enter your name ") # Makes the question variable the new question
    user_details['name'] = not_valid_alphaonly(question) # Gives the not_valid_alphaonly function the question as a parameter and adds the returned string to the dictionary unter name
    print(user_details['name']) # Prints the name
    question = ("Please enter your phone number ") # Makes the question variable the new question
    phone_low = 7 # Makes the variable phone_low the value seven
    phone_high = 10 # Makes the variable phone_high the value 10
    user_details['phonenumber'] = phone_check(question,phone_low,phone_high) # Gives the phone_check function the parameters question, phone_low, and phone_high then adds the returned value to the dictionary user details under phonenumber
    print(user_details['phonenumber']) # Prints the phone number
    question = ("What is your house number? ") # Makes the question variable the new question
    user_details['housenumber'] = not_valid(question) # Gives the not_valid function the question as a parameter and adds the returned answer to the dictionary under housenumber
    print(user_details['housenumber']) # Prints the house number
    question = ("Please enter your street name ") # Makes the question variable the new question
    user_details['streetname'] = not_valid_alphaonly(question) # Gives the not_valid_alphaonly function the parameter question and adds the returned string to the user_details dictionary under streetname
    print(user_details['streetname']) # Prints the street name
    question = ("Please enter your suburb ") # Makes the question variable the new question
    user_details['suburb'] = not_valid_alphaonly(question) # Gives the function not_valid_alphaonly the parameter question and adds the returned answer to the dictionary under suburb
    print(user_details['suburb']) # Prints the suburb
    print("") # Prints a blank line
    print(user_details['name']) # Prints the name from the dictionary
    print(user_details['phonenumber']) # Prints the phone number from the dictionary
    print(user_details['housenumber']) # Printes the house number from the dictionary
    print(user_details['streetname']) # Prints the street name from the dictionary
    print(user_details['suburb']) # Prints the suburb from the dictionary
    print("\n\n\n\n\n\n\n\n\n\n") # Prints ten blank lines

# Prints the Order Menu
# Does not use parameters
def menu(): # Defines the function menu
    table = [] # Creates the blank list table
    count = 0 # Creates the variable count as zero
    print("{: <13}{: <30}{: <6}".format("Item Number","Item","Cost")) # Prints the headings for the table using formating to space them the same distance apart as the table coloumns
    print("{:<13}{:<30}{:<6}".format("- "*6,"- - "*7,"- "*3)) # Prints dashed lines of specific lengths with the same formating as apove for spaceing
    while count in range(len(menu_items)): # Creates a while loop which will compare count and the total amount of items in the menu and loop as long as count is less
        table.append([count+1,menu_items[count],menu_prices[count]]) # Apends the items and their prices and well as an index number to the table list in the corect order and individual rows
        count = count + 1 # Adds one to the count variable so that the while loop runs the correct amount of times 
    for row in table: # Will loop once for every row inside the table list
        print("{: >12} {: <30} ${: <6.2f}".format(*row)) # Prints out each row in coloumns using the row number from the table list (correctly formats each part in coloumns and decimal points for cost)
    print("\n\n\n") # Prints 3 blank lines

# Allows the user to choose how many pizzzas they want to order then gets them to order from the menu
# Does not use any parameters
# Creates a global variable for how many pizzas are ordered and appends orders to two lists item and cost
def ordering(): # Defines the function ordering()
    global order_amount # Makes the variable order_amount global so it can be used outside of this function
    while True: # Creates a while loop which will continue to loop until it is stopped by break
        try: # Trys the following code
            order_count = int(input("How many burgers would you like to order? ")) # Asks the question and makes it an iteger then sets order_count to it if this fails except runs
            if order_count > 0 and order_count <= 40: # Checks if number of burgers ordered is more than zero and less than forty
                order_amount = order_count # Creates the variable order_amount and make it equal to order_count
                break # Stops the while True loop
            elif order_count == 0: # Checks in order_count is 0
                print("You cannot order 0 burgers") # Prints error message saying that zero burgers cannot be ordered
            elif order_count > 40: # Checks if order_count is more than 40
                print("To order more then 40 pizzas please go into store") # Prints error message saying that to order more than 40 pizzas you must go in store
        except ValueError: # Prints error statement if try returns a value error
            print("This cannot be blank and must be a number") # Prints error message
    print("Please use the Item numbers from the menu to order your burgers") # Prints instructions
    print("Please order your burgers individualy") # Prints instructions
    print("") # Prints blank line
    for item in range(order_count): # Runs the same amount of times as the order_count variable
        while order_count > 0: # Creates a while loop which runs as long as order_count is greater then zero
            LOW = 1 # Creates the constant LOW and makes it 1
            HIGH = (len(menu_items)) # Creates th constant HIGH and makes it the amount og itmes in the menu
            if order_count == order_amount: # Checks if the order_count and the order_amount are equal to check if ordering the first item
                question = ("Please enter a number from the menu to order your first burger ") # Sets the question variable to the specified question for the first burger ordered
            else: # Runs if ordering item which is not the first item ordered
                question = ("Please enter a number from the menu to order your next burger ") # Makes the question variable the non-specific question
            order = while_true(LOW,HIGH,question) # Gives the function while_true the parameters LOW, HIGH, and question then makes  the variable order equal the returned value
            order = order - 1 # Removes one from the value of order to account for the difference between how lists first item is 0 and the first index in the menu is 1
            order_count = order_count - 1 # Removes one from the order_count for the loop to show that one order has been completed each time this runs
            order_items.append(menu_items[order]) # Adds the correct item from the menu to the order items using the order number from the while_true function
            order_prices.append(menu_prices[order]) # Adds the correct price for the item to the order_prices list using the count variable
            print("{} ${:.2f}".format(menu_items[order], menu_prices[order])) # Prints order using item name from one list and price from other and formats them with the correct amount of bullet points
            print("")

# Calculates the total delivery charge for if the user choose delivery
# Uses no parameters but does use order_amount and delivery_type global variables
# Adds delivery charge to order_items and order_prices lists
def deliverycharge(): # Defines the function deliverycharge
    if order_amount < 5 and delivery_type == "delivery": # Checks if order amount is less then 5 and the order if for delivery so that the user can be charged
        order_items.append("Delivery Charge") # Adds the delivery charge to the order items for the receipt
        order_prices.append(9) # Adds the delivery cost to the oder prices for the receipt
    elif delivery_type == "delivery": # Runs if last if statement couldn't and delivery type is delivery
        order_items.append("Delivery Charge") # Adds title delivery charge to order_items for receipt
        order_prices.append(0) # Adds the value of 0 to the order prices for delivery charge in receipt

# Prints the receipt for the user
# Uses no parameters but does make use of the dictionary user_details and lists order_items, and order_prices
def receipt_printout(): # Defines the function receipt_printout so it can be called by the code
    totalcost = sum(order_prices) # Makes the variable totalcost the total cost by adding all integers in the order_price list
    table = [] # Creates a empty list names table
    table.append(["User Details","-"*20]) # Adds the title User Details to the table with dashes
    table.append(["Name",user_details['name']]) # Adds the title Name and the name from the user_details dictionary
    table.append(["Phonenumber",user_details['phonenumber']]) # Adds the title Phonenumber and the phonenumber from the user_details dictionary
    if delivery_type == "delivery": # Checks if the order was for delivery
        table.append(["Address","-"*20]) # Adds the title Address and dashes to the table list for the receipt
        table.append(["HouseNumber",user_details['housenumber']]) # Adds the title HouseNumber and the item from the dictironary user_details under housenumber
        table.append(["StreetName",user_details['streetname']]) # Adds the title StreetName and the streetname from the dictionary user_details
        table.append(["Suburb",user_details['suburb']]) # Adds the title Suburb and the suburb from the dictionary user_details
    for row in table: # Runs as many times as their are rows in the table list
        print("{:<15}{:<20}".format(*row)) # Prints each row formated correctly into coloumns
    table = [] # Makes the Table list empty again
    count = 0 # Makes the count variable equal to zero
    print("Order - - - - - - - - - - - - -") # Prints a title for the next part of the receipt
    while count in range(len(order_items)): # Sets up a while loop that will run as long as the variable count corisponds to a item in the list order_items
        table.append([order_items[count],order_prices[count]]) # Adds to the table the correct items from order_items and order_prices using count
        count = count + 1 # Adds one to count to add the next lot of items and prices to the table
    for row in table: # Runs once for each row in the table list
        print("{:<30} ${:<6.2f}".format(*row)) # Prints each row in the list table with the correct formating
    print("Cost - - - - - - - - - - - - - -") # Prints the title Cost
    print("{:<30}${:<6.2f}".format("Total Cost",totalcost)) # Prints the total cost with the title Total cost and correct formating and coloumns

# Allows the user to choose to conacel or confirm their order
# Uses no parametes
def confirm_cancel(): # Defines the function confirm_cancel so it can be called later
    print("To confirm your Budgies Burger order type 1") # Prints the first option
    print("To cancel your order type 2") # Prints the secound option
    LOW = 1 # Creates the constant LOW and sets it to one
    HIGH = 2 # Creates the constant HIGH and sets it to two
    question = ("Please type 1 or 2 ") # Makes the variable question equal to the new question string
    confirmation = while_true(LOW,HIGH,question) # Gives the while_true function the parameters LOW, HIGH, and question makes the variable confirmation the returned value from the function
    if confirmation == 1: # Checks if the order has been confirmed 
        print("Your order has been confirmed") # Prints confirmation message
        if delivery_type == "pickup": # Checks if the order is for pickup
            print("You will recieve a text message when your order is ready to be picked up") # Prints message
        elif delivery_type == "delivery": # Checks if the order is for delivery
            print("Your order will be deliveried shortly") # Prints message
    elif confirmation == 2: # Checks if the order has been canceled
        print("you have canceled your order") # Prints cancel message
    print("")

# Allows the user to choose to either start a new order or exit
# Uses no parameters
def exit(): # Defines the function exit so it can be called
    print("Would you like to restart the program or exit") # Prints the intial question
    print("To exit type 1") # Prints option one
    print("To order again type 2") # Prints option two
    LOW = 1 # Makes the constant LOW and makes it one
    HIGH = 2 # Makes the constant HIGH and makes it two
    question = ("Please enter a number ") # Makes the variable question the new string question
    restart = while_true(LOW,HIGH,question) # Gives the function while_true the parameters LOW, HIGH, and question then makes the variable restat the returned value
    if restart == 1: # Checks if exit has been choosen
        print("Exit") # Prints Exit
        sys.exit() # Ends the program
    elif restart == 2: # Checks if new order has been choosen
        print("\n\n\n\nBegining New Order\n\n\n\n") # Prints New Order title
        user_details.clear() # Clears dictionary
        order_items.clear() # Clears list
        order_prices.clear() # Clears list
        main() # Runs main program from the b egining which starts a new order

# Calls functions in correct order to run the program
def main(): # Defines main function which is the main function and runs everything
    welcome_message() # Calls the function Welcome_message to display welcome message
    order_type() # Calls the function order_type to allow the user to choose pickup or delivery
    menu() # Call the function menu which displays the menu
    ordering() # Calls the function ordering which allows the user to order their burgers
    deliverycharge() # Calls the function deliverycharge to calculate the delivery charge
    receipt_printout() # Calls the function receipt_printout to print out the order
    confirm_cancel() # Calls the function confirm_cancel which allows the user to cancel their order
    exit() # Call the function exit to allows the user to choose to make a new order or not

# Running program
main() # Calls the main function which starts the entire program and ordering system
