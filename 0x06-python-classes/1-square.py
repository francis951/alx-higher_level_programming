#!/usr/bin/python3
"""Define a square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size):
        """Initialization method with a size parameter"""
        self.__size = size

if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)
