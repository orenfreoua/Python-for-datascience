#!/usr/bin/env python3
"""
This module provides a custom implementation of the built-in filter function.
"""

from typing import Callable, Iterable, Any


def ft_filter(function: Callable[[Any], bool], iterable: Iterable) -> list:
    """
    Apply function to each item in iterable and return a list of items
    for which the function returns True.

    :param function: A function that returns True or False.
    :param iterable: An iterable (e.g., list, tuple, etc.).
    :return: A list of elements for which function returns True.
    """
    if not callable(function):
        raise TypeError("First argument must be a callable")
    if not hasattr(iterable, "__iter__"):
        raise TypeError("Second argument must be iterable")

    return [item for item in iterable if function(item)]


def main() -> None:
    """
    Main function for testing purposes.
    This block should not produce output unless explicitly called.
    """
    pass


if __name__ == "__main__":
    main()
