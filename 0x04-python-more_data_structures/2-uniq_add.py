#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to keep track of unique integers
    unique_integers = set()

    # Iterate through the list and add unique integers to the set
    for num in my_list:
        if isinstance(num, int):  # Check if the element is an integer
            unique_integers.add(num)

    # Sum up the unique integers in the set
    result = sum(unique_integers)

    return result
