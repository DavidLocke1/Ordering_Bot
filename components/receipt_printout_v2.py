menu_items = ("Burger Budgie Special","Cheese Burger","Vegetarian Burger","Big Budgie Burger","Itsy-bitsy Burger",
              "Spiced chicken burger","Bacon-beef burger","Mega beef stacker burger","Beef stacker burger",
              "Seafood supreme burger","BBQ Eternal burger","Supreme stacker burger")
menu_prices = (6,4.5,4.5,5,3,5,5,6,5,5,5,6)
order_items = []
order_prices = []
user_details = {'name': 'David', 'phonenumber': '123456789', 'housenumber': '14A', 'streetname': 'Street', 'suburb': 'Hello'}
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

def receipt_printout():
    totalcost = sum(order_prices)
    table = []
    table.append(["User Details","-"*20])
    table.append(["Name",user_details['name']])
    table.append(["Phonenumber",user_details['phonenumber']])
    if delivery_type == "delivery":
        table.append(["Address","-"*20])
        table.append(["HouseNumber",user_details['housenumber']])
        table.append(["StreetName",user_details['streetname']])
        table.append(["Suburb",user_details['suburb']])
    for row in table:
        print("{:<15}{:<20}".format(*row))
    table = []
    count = 0
    print("Order - - - - - - - - - - - - -")
    while count in range(len(order_items)):
        table.append([order_items[count],order_prices[count]])
        count = count + 1
    for row in table:
        print("{:<30} ${:<6.2f}".format(*row))
    print("Cost - - - - - - - - - - - - - -")
    print("{:<30}${:<6.2f}".format("Total Cost",totalcost))

    
    
receipt_printout()