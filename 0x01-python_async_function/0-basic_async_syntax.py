#!/usr/bin/env python3
"""
asynchronous coroutine that takes integer (max_delay) default value = 10
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine wait_random waits for a random delay
    between 0 and max_delay

    Args:
        max_delay(int): amount of maximum time delay in seconds

    Returns:
        delay(float): random delay between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
