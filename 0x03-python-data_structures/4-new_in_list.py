#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 and idx > len(my_list) - 1:
        new_list = my_list.copy()
        return new_list
    else:
        new_list[idx] = element
        return my_list
