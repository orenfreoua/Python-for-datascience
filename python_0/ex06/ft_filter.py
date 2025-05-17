#!/usr/bin/env python3


from typing import Callable, Iterable


def ft_filter(function: Callable[[any], bool], iterable: Iterable) -> list:
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true.
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
