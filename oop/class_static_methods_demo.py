#!/usr/bin/env python3
"""
class_static_methods_demo.py

This script defines the Calculator class to demonstrate the use of
static methods and class methods in Python.
"""

class Calculator:
    """
    A class that provides methods to perform arithmetic operations.
    It includes both a static method and a class method to show their
    different use cases.
    """
    
    # A class attribute that can be accessed by class methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that adds two numbers.
        It doesn't require access to class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that multiplies two numbers.
        It has access to class attributes (via the 'cls' parameter).
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Note: The main execution block is in the separate main.py file.
# This file only contains the class definition.

