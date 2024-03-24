#!/usr/bin/env python3
""" Create an asyncio.Task for the wait_random with the given max_delay """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Arguments:
    - max-delay) (int): Maximum delay for the wait_random coroutine.

    Returns:
    - asyncio.Task : A Task representing the execution of wait_random.
    """

    # Get the current asyncio event loop
    loop = asyncio.get_event_loop()

    # Create an asyncio.Task for the wait_random coroutine,
    # with the specified max_delay
    task = loop.create_task(wait_random(max_delay))

    # Return the created asyncio.Task
    return task
