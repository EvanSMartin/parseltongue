# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_phonebook.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/18 15:29:27 by ispirido          #+#    #+#              #
#    Updated: 2018/07/18 16:22:55 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

from sys import argv

def shared_first(f):
    dictionary = {}
    i = 0
    while 1:
        line = f.readline()
        if not line:
            break
        line = line.strip('\n')
        key = line.split(',')[0]
        dictionary.setdefault(key, [])
        dictionary[key].append(line.split(',')[0])
    print("** Shared First Names! **")
    for key in sorted(dictionary):
        print("{0} ({1}): [{2}]".format(key, len(dictionary[key]),
            ', '.join(dictionary[key])))

def shared_last(f):
    dictionary = {}
    i = 0
    while 1:
        line = f.readline()
        if not line:
            break
        line = line.strip('\n')
        key = line.split(',')[0]
        dictionary.setdefault(key, [])
        dictionary[key].append(line.split(',')[0])
    print("** Shared Last Names **")
    for key in sorted(dictionary):
        print("{0} ({1}): [{2}]".format(key, len(dictionary[key]),
            ', '.join(dictionary[key])))

def main(argv):
    f = open("42.txt", 'r')
    shared_first(f)
    f.close
    print("")
    f = open("42.txt", 'r')
    shared_last(f)
    f.close
main(argv)
