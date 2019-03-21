#!/usr/bin/env python3
import random
import time
import os

width = os.get_terminal_size().columns
tuple = ("Vegetables", "Street names", "Cities", "Breakfast foods", "Gifts", "Flowers", "Ice cream flavors", "Drinks", "Toys", "Nicknames", "Parts of the body", "Hobbies")
l_input = list(range(10))

name = input("Hello, what is your name?\n")
if name:
    print("Welcome,"+name+"!")

question = input("Would you like to play a game? [Y/N]\n").lower().strip()
if question == "n": #in case of capital letters is entered
    print("oh..okay")
    
if question == "y":
    print('List 10 "{}" you know!'.format(random.choice(tuple)))

i = 0
start = time.time()
while i < 10:
    l_input[i] = input("")
    i = i + 1
end = time.time()

i = 0
while i < width:
   print("=", end='')
   i = i + 1
print("\n", end='')

i = 0
while i < 10:
    print("||" + l_input[i].center(width - 4) + "||")
    if i != 9:
        print("||" + "||".rjust(width - 2))
    else:
       j = 0
       while j < width:
           print("=", end='')
           j = j + 1
    i = i + 1
print("Time: {} seconds".format(end - start))
