#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_idx = 0
    for i in range(len(my_list)):
        if my_list[i] >= my_list[max_idx]:
            max_idx = i

    return my_list[max_idx]
