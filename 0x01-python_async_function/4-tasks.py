#!/usr/bin/env python3
""" Concurrently execute the task_wait_random coroutine 'n' times. """
import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Parameters:
    - n (int): Number of times to execute task_wait_random.
    - max_delay (int): Maximum delay for each task_wait_random execution.

    Returns:
    - list: List of delays (float values) in ascending order.
    """
    # Concurrently execute task_wait_random n times
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    # Extract results from tasks and sort them in ascending order
    delays = sorted(task.result() for task in tasks)

    # Returnlist of delays
    return delays
