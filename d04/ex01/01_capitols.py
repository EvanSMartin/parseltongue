# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_capitols.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/18 16:23:21 by ispirido          #+#    #+#              #
#    Updated: 2018/07/18 16:29:58 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

from sys import argv

def main(argv):
    f = open("capitols.txt", 'r')
    d = {}
    while 1:
        line = f.readline()
        if not line:
            break
        line = line.strip('\n')
        d[line.split(',')[0]] = line.split(',')[1]
    while 1:
        usr = input("Ready: ")
        if usr == "Done":
            break
        if usr in d.keys():
            print(d[usr])
        elif usr in d.values():
            for key in d:
                if d[key] == usr:
                    print(key)
        else:
            print("nil")

main(argv)
