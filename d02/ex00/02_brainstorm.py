# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_brainstorm.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ispirido <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/17 11:05:55 by ispirido          #+#    #+#              #
#    Updated: 2018/07/17 11:14:19 by ispirido         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import random
number = 1
answer_list = []
new_list = ["animals", "art", "technology", "clothing", "geography", "history", "holidays", "careers", "movies", "cities"]
counter = 0
print(new_list[number])
while counter < 10:
    answer = input("type an aswer: ")
    answer_list.append(answer)
    counter += 1
counter = 0
while counter <= 9:
    print("||" + answer_list[counter].center(10) + "||")
    counter += 1
