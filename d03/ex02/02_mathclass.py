# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_mathclass.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/13 14:25:36 by ispirido          #+#    #+#              #
#    Updated: 2018/07/16 16:22:30 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import math
from sys import argv

def find_min_max(lst, string):
    return lst[0] if string == "min" else lst[len(lst) - 1]

def find_mean(lst):
    i = 0
    tmp = 0
    while i < len(lst):
        tmp = tmp + lst[i]
        i += 1
    return tmp / len(lst)

def find_median(lst):
    if len(lst) % 2 == 0:
        median = lst[int(len(lst) / 2 - 1)] + lst[int(len(lst) / 2)]
        median = median / 2
    else:
        return lst[math.ceil(len(lst) / 2) - 1]
    return median

def find_mode(lst):
    app = 0
    app_tmp = 0
    i = 0
    save = 0
    while i + 1 < len(lst):
        if lst[i] == lst[i + 1]:
            app_tmp += 1
        elif lst[i] != lst[i + 1] and app < app_tmp:
            app = app_tmp
            save = lst[i]
            app_tmp = 0
        i += 1
    return save if len(lst) > 1 else lst[0]

def find_range(lst):
    return lst[len(lst) - 1] - lst[0]

def main(argv):
    lst = [None] * (len(argv) - 1)
    i = 1
    while i < len(argv):
        lst[i - 1] = argv[i]
        lst[i - 1] = int(lst[i - 1])
        i += 1
    lst.sort()
    global save
    print("Min: {0}\nMax: {1}".format(find_min_max(lst, "min"), find_min_max(lst, "max")))
    print("Mean: {0}\nMedian: {1}".format(find_mean(lst), int(find_median(lst))))
    print("Mode: {0}\nRange: {1}".format(find_mode(lst), find_range(lst)))
    find_median(lst)

if __name__ == '__main__':
    main(argv)
