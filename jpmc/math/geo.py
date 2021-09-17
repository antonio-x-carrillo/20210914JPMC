"""
Misc geometric functions

Also has PI as a convenient variable.

Blah blah blah-dy blah
"""
import math

PI = math.pi

class Dog:
    """
    Represent one of our canine friends
    """
    def bark(self):
        print("woof woof")

def circle_area(diameter):
    """
    Compute area of circle given a diameter

    :param diameter: Diameter of circle (NOT radius)
    :return: Area of circle as a float
    """
    return ((diameter / 2) ** 2) * math.pi

def rectangle_area(length, width):
    """
    Compute area of rectangle

    :param length: Length of side
    :param width:  Length of other side
    :return:
    """
    return length * width

def square_area(side):
    """
    Compute area of square

    :param side:
    :return:
    """
    return rectangle_area(side, side)

