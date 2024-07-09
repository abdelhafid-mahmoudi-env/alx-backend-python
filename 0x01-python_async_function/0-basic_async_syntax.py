#!/usr/bin/env python3
"""
    The basics of async.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive) seconds 
    and eventually returns the delay value.
    
    Args:
        max_delay (int): Maximum value for the random delay.
    
    Returns:
        float: The duration of the random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
