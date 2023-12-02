#!/usr/bin/python3
def element_at(my_list, idx):
    # Checks if its integer
    if idx < 0:
        return None
    # Checks if idx is with thr ranged
    elif idx > len(my_list):
        return None
    # returns idx at the specied index
    else:
        return my_list[idx]
