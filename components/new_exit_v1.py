import sys

user_details = {123123}
order_items = [123123213,"123213"]
order_prices = []

def exit():
    print("Would you like to restart the program or exit")
    print("To exit type 1")
    print("To order again type 2")
    while True:
        try:
            restart = int(input("Please enter a number "))
            if restart == 1:
                print("Exit")
                sys.exit()
            elif restart == 2:
                print(user_details)
                print(order_items)
                print("\n\n\n\nBegining New Order\n\n\n\n")
                user_details.clear()
                order_items.clear()
                order_prices.clear()
                print(user_details)
                print(order_items)
                main()
                break
            else:
                print("number must be 1 or 2")
        except ValueError:
            print("You must enter 1 or 2 to exit or start a new order")


def main():
    exit()

main()