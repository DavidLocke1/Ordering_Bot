
menu_items = ("Burger Budgie Special","Cheese Burger","Vegetarian Burger","Big Budgie Burger","Itsy-bitsy Burger",
              "Spiced chicken burger","Bacon-beef burger","Mega beef stacker burger","Beef stacker burger",
              "Seafood supreme burger","BBQ Eternal burger","Supreme stacker burger")
menu_prices = (6,4.5,4.5,5,3,5,5,6,5,5,5,6)

def menu():
    table = []
    count = 0
    #menu_max_length = 0
    while count in range(len(menu_items)):
        table.append([count+1,menu_items[count],menu_prices[count]])
        #item_length = len(menu_items[count])
        #if item_length > menu_max_length:
        #    menu_max_length = item_length
        count = count + 1
    for row in table:
        print("{: >5} {: <30} ${: <6.2f}".format(*row))

menu()