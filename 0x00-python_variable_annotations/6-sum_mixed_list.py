#!/usr/bin/env python3
"""  This function returns the sum of a list of integers and float numbers """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Parameters:
    mxd_lst (List[Union[int, float]]): The list of integers and float numbers.

    Returns:
    float: The sum of the numbers in the list.
    """
    return float(sum(mxd_lst))
