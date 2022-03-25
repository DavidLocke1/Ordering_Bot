print("")

valid = False
while not valid:
        name = input("Please enter your name")
        if name != "":
            print(name)
            break
        else:
            print("Sorry this cannot be blank")

valid = False
while not valid:
    phonenumber = input("Please enter your phone number")
    if phonenumber != "":
        print(phonenumber)
        break
    else:
        print("Sorry this cannot be blank")

print(name)
print(phonenumber)
