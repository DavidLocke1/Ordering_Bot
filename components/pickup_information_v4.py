user_details = {}

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
user_details['name'] = not_valid(question)
print(user_details['name'])

question = ("Please enter your phone number ")
user_details['phonenumber'] = not_valid(question)
print(user_details['phonenumber'])



print(user_details)
print(user_details['name'])
print(user_details['phonenumber'])
