#!/usr/bin/env python3
"""
book_class.py

This script defines the Book class with magic methods for initialization,
destruction, and string representation.
"""

class Book:
    """
    A class to represent a book with its title, author, and publication year.
    It includes magic methods to handle object creation, deletion, and
    string representations.
    """
    
    def __init__(self, title, author, year):
        """
        Constructor to initialize a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year.
        """
        self.title = title
        self.author = author
        self.year = year
        # The print statement has been removed to match the expected output.

    def __del__(self):
        """
        Destructor that is called when a Book object is about to be destroyed.
        It prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns an informal string representation of the Book object.
        This is typically used for a user-friendly display.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation of the Book object.
        The string is in a format that could be used to recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

