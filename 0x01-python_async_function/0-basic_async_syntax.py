#!/usr/bin/env python3
""" Asynchronous coroutine that waits for a random delay and returns it. """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Arguments:
    - max-delay (int): Maximum delay in seconds (default value is 10).

    Returns:
    - float: Random delay between 0 and max_delay seconds
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
