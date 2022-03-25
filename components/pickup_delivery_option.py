from operator import truediv

print("Would you like your order for pickup or delivery")
print("Type 1 for pickup")
print("Type 2 for delivery")

while True:
    try:
        delivery_option = int(input())
        if delivery_option == 1:
            print("Is equal to 1")
            break
        elif delivery_option == 2:
            print("is equal to 2")
            break
        else:
            print("must be number from allowed")
    except ValueError:
        print("value error")

