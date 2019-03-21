# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_parentheses.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/02 11:57:36 by ispirido          #+#    #+#              #
#    Updated: 2018/07/13 16:36:43 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python
from sys import argv

def check_parentheses(string):
    opening = 0
    closing = 0
    for char in string:
        if char == "(":
            opening += 1
        elif char == ")":
            closing += 1
    return opening == closing


def main():
    out = ""
    if len(argv) > 1:
        loc = 0
        for i in range(len(argv[1])):
            if argv[1][i].isalpha():
                if loc % 2 == 0:
                    out += argv[1][i].upper()
                else:
                    out += argv[1][i].lower()
                loc += 1
            else:
                out += argv[1][i]
        print(out)
        prev = out
        out = ""
        for i in range(len(prev)):
            if prev[i].isupper() and prev[i] in "AEIOU":
                out += "*"
            else:
                out += prev[i]
        print(out)
        print("Balanced? {}".format(check_parentheses(argv[1])))

if __name__ == '__main__':
    main()
