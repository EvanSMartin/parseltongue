# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    04_bool.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/26 13:08:21 by ispirido          #+#    #+#              #
#    Updated: 2018/06/26 15:37:31 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

import random

a = ["False","True","True","None","True","None","None","False","False","None","True","False"]
b = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"]
c = ["False","False","None","None","True","True","False","True","None","False","True","None"]

a_random = random.choice(a)
b_random = random.choice(b)
c_random = random.choice(c)

print("{0} {1} {2} => ".format(a_random, b_random, c_random), end="")
if b_random == "or":
    print(a_random or c_random)
elif b_random == "!=":
    print(a_random != c_random)
elif b_random == "and":
    print(a_random and c_random)
elif b_random == "==":
    print(a_random == c_random)
