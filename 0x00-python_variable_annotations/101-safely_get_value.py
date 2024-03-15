#!/usr/bin/env python3
""" duck type annotation """
from typing import Mapping, Union, Any


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """ type annotated func """
    if key in dct:
        return dct[key]
    else:
        return default
