user_details = {}

def not_valid_alphaonly(question):
    valid = False
    while not valid:
        print("")
        answer = input(question)
        if answer != "" and answer.isalpha():
            return answer.title()
        elif answer != "":
            print("Answer must not include numbers or spaces")
        else:
            print("Sorry this cannot be blank")

def not_valid_numonly(question):
    valid = False
    while not valid:
        print("")
        answer = input(question)
        if answer != "" and answer.isnumeric():
            return answer.title()
        elif answer != "":
            print("Answer must not include letters or spaces")
        else:
            print("Sorry this cannot be blank")
        
def not_valid(question):
    valid = False
    while not valid:
        print("")
        answer = input(question)
        if answer != "":
            return answer.title()
        else:
            print("Sorry this cannot be blank")
    

question = ("Please enter your name ")
user_details['name'] = not_valid_alphaonly(question)
print(user_details['name'])

question = ("Please enter your phone number ")
user_details['phonenumber'] = not_valid_numonly(question)
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
print(user_details[''])
print(user_details[''])
print(user_details[''])
