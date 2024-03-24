#!/usr/bin/env python3
""" Safely gets a value from a dictionary. """
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:

    """
    Parameters:
    - dct (Mapping): The input dictionary.
    - key (Any): The key to retrieve from the dictionary.
    - default (Union[T, None], optional): The default value to return if the,
      key is not present. Defualt to None

    Returns:
    - Union[Any, T]: The value associated with the key,
                     or the default value if the key is not present.
    """
    if key in dict:
        return dct[key]
    else:
        return default
