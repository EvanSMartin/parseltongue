#!/usr/bin/env python3
import random

number = random.randint(1, 10)
tries = 0
win = False # setting a win flag to false

name = raw_input("Hello, what is your name?\n")
if name:
    print("Welcome,"+name+"!")

question = raw_input("Would you like to play a game? [Y/N]\n").lower().strip()
if question == "n": #in case of capital letters is entered
    print("oh..okay")
    
if question == "y":
    print("I'm thinking of a number between 1 & 10")

    while not win: # while the win is not true, run the while loop. 
        guess = int(raw_input("Have a guess: "))
        tries = tries + 1
        if guess == number:
            win = True # set win to true when the user guesses correctly.
            print("Congrats, you guessed correctly! The number was indeed {}".format(number))
            print("it had taken you {} tries".format(tries))
        elif guess < number:
            print("Guess higher...")
        elif guess > number:
            print("Guess lower...")
