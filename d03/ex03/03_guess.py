# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03_guess.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/16 16:24:15 by ispirido          #+#    #+#              #
#    Updated: 2018/07/17 10:54:56 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

from sys import argv
import random

def main(argv):
    i = 10
    words = ["jazzy", "quick", "dizzy", "apple", "pizza"]

    word = random.choice(words)
    print("The secret word begins with {}".format(word[0].upper()))
    while i >= 0:
        i -= 1
        answer = input("Guess: ").lower()
        if len(answer) == 0:
            print("You wasted a guess =P")
        elif len(answer) != 5:
            print("0, 1, 2, 3, 4, 5 that's how we count to five!")
        elif len(answer) == 5 and answer[0] != word[0]:
            alphabet = ""
            for letter in range(97, 123):
                alphabet += chr(letter)
            print(alphabet)
        elif answer[0] == word[0] and len(answer) == 5:
            if answer != word:
                print("You have {} guesses left!".format(i))
            else:
                print("Good Job! You are one with the Source.")
                exit ()

if __name__ == '__main__':
    main(argv)
