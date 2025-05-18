#!/usr/bin/env python3

import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:
    """
    Compute the Body Mass Index (BMI) for each height/weight pair.
    """
    # Check input types
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both arguments must be lists.")

    if len(height) != len(weight):
        raise ValueError("Both lists must have the same length.")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError(
                "All elements must be integers or floats."
            )
        if h <= 0:
            raise ValueError("Height must be strictly positive.")
        if w <= 0:
            raise ValueError("Weight must be strictly positive.")

    h_array = np.array(height)
    w_array = np.array(weight)
    bmi_array = w_array / (h_array ** 2)
    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of booleans: True if the BMI is above the limit.
    """
    if not isinstance(bmi, list):
        raise TypeError("The first argument must be a list.")

    if not isinstance(limit, int):
        raise TypeError("The limit must be an integer.")

    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError(
                "All elements in the BMI list must be int or float."
            )

    bmi_array = np.array(bmi)
    result = bmi_array > limit
    return result.tolist()


def main():
    """
    Main function for testing purposes.
    This block should not produce output unless explicitly called.
    """
    pass


if __name__ == "__main__":
    main()
