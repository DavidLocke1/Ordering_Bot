print("To confirm your Budgies Burger order type 1")
print("To cancel your order type 2")
while True:
    try:
        confirmation = int(input("Please type 1 or 2 "))
        if confirmation == 1:
            print("Your order has been confirmed")
            break
        elif confirmation == 2:
            print("you have canceled your order")
            break
        else:
            print("please enter 1 or 2")
    except ValueError:
        print("you must enter a number between 1 and 2 for confirm or cancel")

        