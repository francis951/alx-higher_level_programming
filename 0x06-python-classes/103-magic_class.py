#!/usr/bin/python3
"""Define a MagicClass class"""


class MagicClass:
    """Class that matches the provided Python bytecode"""

    def __init__(self, radius=0):
        """Initialization method with optional radius parameter"""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Compute and return the area of the circle"""
        return (self.__radius ** 2) * 3.14159265359

    def circumference(self):
        """Compute and return the circumference of the circle"""
        return 2 * 3.14159265359 * self.__radius
