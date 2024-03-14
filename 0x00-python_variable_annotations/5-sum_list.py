#!/usr/bin/env python3
"""type-annotated func retuns sum of lost of floats."""


def sum_list(input_list: list[float]) -> float:
    """type-annotated func retuns sum of lost of floats."""
    x: float = 0.0
    for num in input_list:
        x += num
    return x
