#!/usr/bin/env python3
""" A function that multiplies a float by a given multiplier. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Parameters:
    multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: A function that takes a float and returns a float
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
