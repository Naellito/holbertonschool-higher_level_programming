#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    if idx < 0:
        return (my_list)
    if idx > len(my_list):
        return (my_list)
    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element
    return (my_list)
