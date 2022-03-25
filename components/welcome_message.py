import random
from random import randint
from tkinter import N

names = ["Mark", "Pheobe", "Sally", "Michael", "Denise",
         "Ellen", "Eris", "Moana", "Lewis", "Lara"]

def welcome_message():
    num = randint(0,len(names)-1)
    name = (names[num])

    print("* * * * * * * *")
    print(" *")
    print("* *  Welcome to Budgie's burger's")
    print(" *   My name is ", name)
    print("* *  I am here to take your order")
    print(" *")
    print("* * * * * * * *")
    print("")