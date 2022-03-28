user_details = {}

def not_valid_alphaonly(question):
    valid = False
    while not valid:
        print("")
        answer = input(question)
        if answer != "" and any(x.isnumeric() for x in answer) == False:
            return answer.title()
        elif answer != "":
            print("Answer must not include numbers")
        else:
            print("Sorry this cannot be blank")

def phone_check(question,phone_low,phone_high):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= phone_low and count <= phone_high:
                return str(num)
            else:
                print("Phone numbers have between 7 and 10 digits")
        except ValueError:
            print("Please enter a number")
        
question = ("Please enter your name ")
user_details['name'] = not_valid_alphaonly(question)
print(user_details['name'])

question = ("Please enter your phone number ")
phone_low = 7
phone_high = 10
user_details['phonenumber'] = phone_check(question,phone_low,phone_high)
print(user_details['phonenumber'])

print("")
print(user_details['name'])
print(user_details['phonenumber'])
