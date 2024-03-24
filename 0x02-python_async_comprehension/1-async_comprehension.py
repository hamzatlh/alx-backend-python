#!/usr/bin/env python3
"""
Asynchronous coroutine that collects 10 random numbers using,
an async comprehension over async_generator.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns:
    - List[float]: A list of 10 random floating-point numbers between 0 and 10
    """

    # Use an async comprehension to collect 10 random floating number b/n 1-10
    result = [number async for number in async_generator()]
    return result
