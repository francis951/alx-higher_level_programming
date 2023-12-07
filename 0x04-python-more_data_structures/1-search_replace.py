#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the elements in the original list
    for element in my_list:
        # If the element matches the 'search' element, replace it with 'replace'
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    return new_list
