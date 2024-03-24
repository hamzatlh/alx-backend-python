#!/usr/bin/env python3
""" This function returns the sum of a list of float numbers. """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Parameters:
    input_list (List[float]): The list of float numbers.

    Returns:
    float: The sum of the float numbers in the list.
    """
    return sum(input_list)
