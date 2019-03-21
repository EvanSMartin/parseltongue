# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_arrmatey.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/20 15:29:25 by ispirido          #+#    #+#              #
#    Updated: 2018/06/21 13:25:43 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

print("Argv of 0 is", argv[1])
print("Argv of 1 is", argv[2])
print("Argv of 2 is", argv[3])
print("Argv of 3 is", argv[4])
print("Argv of 4 is", argv[5])
print("Argv of 5 is", argv[6])
print("Argv of 6 is", argv[7])
print("Argv of 7 is", argv[8])
print("Argv of 8 is", argv[9])

argv.sort(key=len, reverse=True)
print(argv[1])
print(argv[2])
print(argv[3])
print(argv[4])
print(argv[5])
print(argv[6])
print(argv[7])
print(argv[8])
print(argv[9])
