# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_allyourbase.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/18 16:30:17 by ispirido          #+#    #+#              #
#    Updated: 2018/07/18 16:35:56 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

from sys import argv

def base_conversation(decimal, base):
    number = int(decimal)
    string = ''
    conversation = '0123456789ABCDEF'
    while number > 0:
        string = conversation[(int(number % base))] + string
        number = int(number / base)
    print(string)

def main(argv):
    if len(argv) != 2:
        print("usage: ./python3 [name of the program] [decimal]")
        exit (0)
    base_conversation(argv[1], 2)
    base_conversation(argv[1], 8)
    base_conversation(argv[1], 16)
main(argv)
