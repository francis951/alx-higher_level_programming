def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None
    
    # Initialize the max_value with the first element of the list
    max_value = my_list[0]
    
    # Iterate through the list to find the maximum value
    for num in my_list:
        if num > max_value:
            max_value = num
    
    return max_value
