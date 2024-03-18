#!/usr/bin/env python3
""" async function puthon """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ async function python """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    elapsed = end - start
    return elapsed / n
