#!/usr/bin/env python3
""" function’s parameters that return values with the appropriate types """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates and returns a list of tuples,
    each containing an element from 'lst' and its length.

    Parameters:
    - lst (Iterable[Sequence]): Input iterable of sequences.

    Returns:
    - List[Tuple[Sequence, int]]: List of tuples with element and its length.
    """
    return [(i, len(i)) for i in lst]
