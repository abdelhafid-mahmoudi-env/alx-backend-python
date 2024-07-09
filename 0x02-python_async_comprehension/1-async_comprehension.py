#!/usr/bin/env python3
"""
This module defines a coroutine async_comprehension
that collects random numbers using async comprehensions.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator.
    Returns:
        A list of 10 random float numbers.
    """
    return [i async for i in async_generator()]
