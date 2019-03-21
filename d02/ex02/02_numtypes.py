# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_numtypes.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/21 13:25:56 by ispirido          #+#    #+#              #
#    Updated: 2018/06/26 13:53:10 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
a = 10
b = 56.99
c = 2+3j
res = int(arg1) // int(arg2)
rem = int(arg1) % int(arg2)
print("{} devided by {} equals {} reminder {}".format(arg1, arg2, res, rem))
print("Variable a contains: {} which is of type: {}".format(a, type(a)))
print("Variable b contains: {} which is of type: {}".format(b, type(b)))
print("Variable c contains: {} which is of type: {}".format(c, type(c)))
