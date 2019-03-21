# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_arrmatey.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/17 11:15:38 by ispirido          #+#    #+#              #
#    Updated: 2018/07/17 11:17:39 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

from sys import argv

for i in range(len(argv)):
    print("Argv of {} is {}".format(i, argv[i]))

argv.sort(key=len, reverse=True)

for i in argv:
    print(i)
