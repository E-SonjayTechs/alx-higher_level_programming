#!/usr/bin/python3

def element_at(my_list, id_x):
    if id_x < 0 or id_x > len(my_list) - 1:
        return 'None'
    else:
        return my_list[id_x]
