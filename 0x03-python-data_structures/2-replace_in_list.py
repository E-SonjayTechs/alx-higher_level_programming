#!/usr/bin/python3

def replace_in_list(my_list, id_x, element):
    if id_x < 0 or id_x > len(my_list) - 1:
        return my_list
    else:
        my_list[id_x] = element
        return my_list
