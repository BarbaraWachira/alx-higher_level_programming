#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    def _init_(self, width=0, height=0):
        """Initialize a new Rectangle
        Args:
           width (int): The width of new rectangle.
           Height(int): The height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Get/set the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
