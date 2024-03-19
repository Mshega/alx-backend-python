#!/usr/bin/env python3
"""
Task 1-concurrent_coroutines
"""
from typing import List
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
