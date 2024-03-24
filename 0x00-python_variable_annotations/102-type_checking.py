#!/usr/bin/env python3
""" Module for zooming elements in a tuple. """
from typing import Tuple, List, Any


""" Function to zoom an array """


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a new list
    where each item in the original list is repeated 'factor' times
    """
    zoomed_in = [
            # For each item in the original list
            item for item in lst
            # Repeat 'factor' times
            for i in range(factor)
    ]
    """ Return the new zoomed in list """
    return zoomed_in


""" Define an array as a tuple """
array = (12, 72, 91)

""" Call the zoom_array function with the array and default factor of 2 """
zoom_2x = zoom_array(array)

""" Call the zoom_array function with the array and a factor of 3 """
zoom_3x = zoom_array(array, 3)
