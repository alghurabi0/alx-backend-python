#!/usr/bin/env python3
"""type-annotated func retuns sum of lost of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """type-annotated func retuns sum of lost of floats."""
    x: float = 0.0
    for num in input_list:
        x += num
    return x
