#!/usr/bin/env python3
"""type-annotated func returns sum of ints and floats in list."""


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """type-annotated func returns sum of ints and floats in list."""
    x: float 0.0
    for num in mxd_lst:
        x += num
    return x
