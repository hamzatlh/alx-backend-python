#!/usr/bin/env python3
""" Measure the total execution time for wait_n and return total_time / n. """
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Arguments:
    - n (int): Number of times to execute wait_n.
    - max_delay (int): Maximum delay for each wait_n execution.

    Returns
    - float: Average execution time per wait_n execution
    """
    # Measure the start time
    start_time = time.time()

    # Run wait_n asyncronously
    asyncio.run(wait_n(n, max_delay))

    # Measure the end time
    end_time = time.time()

    # Calculate the total execution time
    total_time = end_time - start_time

    # Calculate and return the average execution time per wait_n execution.
    return total_time / n
