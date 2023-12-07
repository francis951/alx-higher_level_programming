#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use set symmetric difference to find elements present in only one set
    return set_1.symmetric_difference(set_2)
