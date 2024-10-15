#!/usr/bin/env python3
"""
task_wait_random that takes an integer max_delay and returns a asyncio.Task
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: The task wrapping the wait_random coroutine.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
