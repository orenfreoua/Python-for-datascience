import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list using the start and end indices provided.
    """
    # Check if input is a list
    if not isinstance(family, list):
        raise TypeError("Input must be a list of lists.")
    # Check if it's a 2D list and all sublists have the same length
    if not all(isinstance(row, list) for row in family):
        raise TypeError("All elements of the input must be lists.")

    # Get the length of the first sublist
    expected_length = len(family[0])

    # Check all other sublists
    for i, row in enumerate(family):
        if len(row) != expected_length:
            raise ValueError("Sublists must all have the same length.")

    # Convert to numpy array for easy shape handling and slicing
    array = np.array(family)
    print(f"My shape is : {array.shape}")

    # Slice the array
    new_array = array[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()


def main():
    """
    Main function for testing purposes.
    This block should not produce output unless explicitly called.
    """
    pass


if __name__ == "__main__":
    main()
