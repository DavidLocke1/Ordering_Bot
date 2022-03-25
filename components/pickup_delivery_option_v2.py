from operator import truediv
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
order_type()