#!/usr/bin/env python3

from PIL import Image      # Library to open and manipulate images
import numpy as np         # Library for working with arrays
import os                  # Used to check if file exists

def ft_load(path: str):
    """
    Load an image from a given file path and return its RGB pixels as a NumPy array.
    Only supports JPG and JPEG formats.
    """
    try:
        # Check if the file exists
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Error: File '{path}' not found.")

        # Open the image using PIL
        with Image.open(path) as img:
            # Check if the image format is supported
            if img.format not in ["JPEG", "JPG"]:
                raise ValueError(f"Error: Unsupported image format '{img.format}'. Only JPG and JPEG are allowed.")
            
            # Convert the image to RGB (if not already)
            img = img.convert("RGB")
            
            # Convert the image to a NumPy array
            array = np.array(img)
            
            # Print the shape of the array (height, width, channels)
            print(f"The shape of image is: {array.shape}")
            
            # Return the image as a NumPy array
            return array

    except Exception as e:
        # Print the error message and return None if something goes wrong
        print(e)
        return None

def main():
    """
    Main function for testing purposes.
    This block should not produce output unless explicitly called.
    """
    pass


if __name__ == "__main__":
    main()
