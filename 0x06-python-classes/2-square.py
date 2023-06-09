#!/usr/bin/python3
<<<<<<< HEAD

"""Define a class Square."""
class Square:
    """
    This class represents a square.
=======
"""Define a class Square."""

>>>>>>> cf59dac8a4f2fda70e894784cd98ccb69e84ed27

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

