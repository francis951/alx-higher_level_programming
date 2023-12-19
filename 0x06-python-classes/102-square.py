#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialization method with optional size parameter"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def __lt__(self, other):
        """Less than (<) comparator based on square area"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to (<=) comparator based on square area"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal to (==) comparator based on square area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal to (!=) comparator based on square area"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than (>) comparator based on square area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to (>=) comparator based on square area"""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
