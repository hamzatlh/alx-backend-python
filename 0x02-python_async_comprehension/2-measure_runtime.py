#!/usr/bin/env python3
"""
Asynchronous coroutine that executes async_comprehension,
four times in parallel using asyncio.gather.
"""
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns:
    - float: Total runtime fot the four executions in seconds.
    """

    # Record the start time
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    # Record the end time
    end_time = asyncio.get_event_loop().time()

    # Calculate and return the total runtime
    return end_time - start_time
