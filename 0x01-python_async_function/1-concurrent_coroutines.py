#!/usr/bin/env python3
""" async function python """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ async function python """
    lst = []
    i: int = 0
    while i < n:
        task = asyncio.create_task(wait_random(max_delay))
        lst.append(task)
        i += 1

    return [await task for task in asyncio.as_completed(lst)]
