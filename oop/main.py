#!/usr/bin/env python3
"""
main.py

This script tests the functionality of the classes in polymorphism_demo.py
by creating instances of Rectangle and Circle and invoking their area() method.
"""

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # Create a list of different shape objects
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Iterate through the list and calculate the area for each shape
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()


