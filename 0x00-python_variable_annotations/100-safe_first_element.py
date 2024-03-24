#!/usr/bin/env python3
"""
A function that Returns the first element of the list if it exists,
other wise returns None
"""
from typing import Optional, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Parameters:
    - lst (Sequence[Any]): Input sequence.

    Returns:
    - Optional[Any]: The first element of the sequence or,
      None if the sequence is empty.
    """

    if lst:
        return lst[0]
    else:
        return None
