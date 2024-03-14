#!/usr/bin/env python3
""" type-annotated func """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ type-annotated func """
    return (k, float(v**2))
