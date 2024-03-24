#!/usr/bin/env python3
""" This function takes a string and an int/float, and returns a tuple. """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Parameters:
    k (str): The string.
    v (Union[int, float]): The int or float number.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string k and,
    the second element is the square of v.
    """
    return k, float(v**2)
