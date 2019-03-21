# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_rainbow.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/26 16:11:40 by ispirido          #+#    #+#              #
#    Updated: 2018/07/03 12:05:48 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys

def print_colorful_text(string, style, foreground, background):
    codes = []
    for letter in string:
        color_code = ";".join([str(style), str(foreground), str(background)])
        codes.append(f"\x1b[{color_code}m {letter}  \x1b[0m")
        foreground+=1
        background+=1
    print("".join(codes))

def main(args):
    if len(args) == 5:
        print_colorful_text(args[1], int(args[2]), int(args[3]), int(args[4]))

if __name__ == "__main__":
    main(sys.argv)
