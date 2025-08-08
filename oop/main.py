#!/usr/bin/env python3
"""
main.py

This script tests the Calculator class's static and class methods,
demonstrating their functionality and how they are called.
"""

from class_static_methods_demo import Calculator

def main():
    # Using the static method to add two numbers
    # Note: Static methods are called directly on the class without an instance.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method to multiply two numbers
    # Note: Class methods are also called on the class and have access to
    # class-level attributes like `calculation_type`.
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()

