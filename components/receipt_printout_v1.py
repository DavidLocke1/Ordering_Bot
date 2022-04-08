menu_items = ("Burger Budgie Special","Cheese Burger","Vegetarian Burger","Big Budgie Burger","Itsy-bitsy Burger",
              "Spiced chicken burger","Bacon-beef burger","Mega beef stacker burger","Beef stacker burger",
              "Seafood supreme burger","BBQ Eternal burger","Supreme stacker burger")
menu_prices = (6,4.5,4.5,5,3,5,5,6,5,5,5,6)
order_items = []
order_prices = []
user_details = {'name': 'David', 'phonenumber': '123456789','housenumber': '14A', 'streetname': 'Street', 'suburb': 'Hello'}

test = int(input("1 or 2"))
if test == 1:
    delivery_type = "pickup"
else:
    delivery_type = "delivery"

print("123214124214")
count = 5
while count >= 0:
    order_items.append(menu_items[count])
    order_prices.append(menu_prices[count])
    count = count - 1
#print("123123123123")
#def receipt_printout():
#    for row in order_items:
#        print("{:<20}{:>10}".format, order_items[row], order_prices[row])

#receipt_printout()
def receipt_printout():
    table = []
    count = 0
    while count in range(len(order_items)):
        table.append([order_items[count],order_prices[count]])
        count = count + 1

    for row in table:
        print("{: <30} ${: <6.2f}".format(*row))

    table = []
    if delivery_type == "delivery":
        table.append(["Name",user_details['name']])
        table.append(["Phonenumber",user_details['phonenumber']])
        table.append(["HouseNumber",user_details['housenumber']])
        table.append(["StreetName",user_details['streetname']])
        table.append(["Suburb",user_details['suburb']])

    else:
        table.append(["Name",user_details['name']])
        table.append(["Phonenumber",user_details['phonenumber']])


    for row in table:
        print(*row)
receipt_printout()