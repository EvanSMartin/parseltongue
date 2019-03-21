# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_rainbow.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/18 16:42:26 by ispirido          #+#    #+#              #
#    Updated: 2018/07/18 16:45:32 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def print_format_table():
    i = 0
    s2 = "RAINBOW"
    s1 = ""
    for fg in range(30,37):
        format = ';'.join(['6', str(fg), '47'])
        s1 += '\x1b[%sm %s \x1b[0m' % (format, s2[i])
        i += 1
    print(s1)
print_format_table()
