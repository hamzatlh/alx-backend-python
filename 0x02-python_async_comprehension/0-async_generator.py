#!/usr/bin/env python3
""" Asyncronous generator that yields a random number between 0 and 10 """
import asyncio
import random
from typing import Generator, Optional


async def async_generator() -> Generator[float, Optional[None], None]:
    """
    Asyncronous generator that yields a random number between 0 and 10

    Yields:
    - float: A random floating-point number between 0 and 10
    """
    # Loop 10 times to yield 10 random numbers
    for _ in range(10):
        # Asyncronously wait for 1 second
        await asyncio.sleep(1)
        # Using uniform for floating-point number
        yield random.uniform(0, 10)
