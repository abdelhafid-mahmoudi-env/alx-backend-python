#!/usr/bin/env python3
"""
Module for element_length function
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with elements and their lengths.

    Args:
        lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with elements and their lengths.
    """
    return [(i, len(i)) for i in lst]
