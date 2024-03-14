#!/usr/bin/env python3
"""type-annotated func"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annoatted func"""
    return lambda x: x * multiplier
