#!/usr/bin/env python3
"""type-annotated func"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """type annotated func """
    return [(i, len(i)) for i in lst]
