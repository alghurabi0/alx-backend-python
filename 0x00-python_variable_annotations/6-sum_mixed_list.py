#!/usr/bin/env python3
"""type-annotated func returns sum of ints and floats in list."""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """type-annotated func returns sum of ints and floats in list."""
    x: float 0.0
    for num in mxd_lst:
        x += num
    return x
