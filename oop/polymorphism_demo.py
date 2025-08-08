#!/usr/bin/env python3
"""
polymorphism_demo.py

This script demonstrates polymorphism and method overriding by
defining a base Shape class and derived Rectangle and Circle classes.
"""

import math

class Shape:
    """
    A base class for all shapes.
    It defines a method 'area' that must be implemented by subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by derived classes.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    """
    A class for a rectangle, inheriting from Shape.
    It overrides the area method to calculate the area of a rectangle.
    """
    def __init__(self, length, width):
        """
        Initializes a Rectangle with a length and a width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class for a circle, inheriting from Shape.
    It overrides the area method to calculate the area of a circle.
    """
    def __init__(self, radius):
        """
        Initializes a Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle using math.pi.
        """
        return math.pi * self.radius ** 2

# Note: The main execution block is in the separate main.py file.
# This file only contains the class definitions.

