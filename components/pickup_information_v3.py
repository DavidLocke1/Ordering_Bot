user_details = {}

print("")

valid = False
while not valid:
        user_details['name'] = input("Please enter your name")
        if user_details['name'] != "":
            print(user_details['name'])
            break
        else:
            print("Sorry this cannot be blank")

valid = False
while not valid:
    user_details['phonenumber'] = input("Please enter your phone number")
    if user_details['phonenumber'] != "":
        print(user_details['phonenumber'])
        break
    else:
        print("Sorry this cannot be blank")

print(user_details)
print(user_details['name'])
print(user_details['phonenumber'])
