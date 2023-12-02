def delete_at(my_list=[], idx=0):
    # Check if the index is out of range or negative
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the same list if index is invalid
    
    # Create a new list with elements before and after the specified index
    new_list = my_list[:idx] + my_list[idx+1:]
    
    return new_list
