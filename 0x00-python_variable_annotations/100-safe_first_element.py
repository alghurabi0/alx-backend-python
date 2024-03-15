#!/usr/bin/env python3
""" duck type annotation """
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ duck annotation type """
    if lst:
        return lst[0]
    else:
        return None
