#!/usr/bin/env python3
""" async function python """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ async function python """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
