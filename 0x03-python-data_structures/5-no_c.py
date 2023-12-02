#!/usr/bin/python3
def no_c(my_string):
    for i in list(my_string):
        if i == 'c':
            list(my_string).remove(i)
        elif i == 'C':
            list(my_string).remove(i)
        else:
            return(''.join(list(my_string)))
