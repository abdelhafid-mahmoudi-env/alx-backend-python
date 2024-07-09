#!/usr/bin/env python3
""" Asynchronous Basics """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Creates an asyncio task to wait for a random delay."""
    tsk = create_task(wait_random(max_delay))
    return tsk
