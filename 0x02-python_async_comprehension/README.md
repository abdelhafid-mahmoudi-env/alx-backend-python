# 0x02. Python - Async Comprehension

## Project Overview
This project covers asynchronous comprehensions in Python, including writing asynchronous generators, using async comprehensions, and type-annotating generators. The aim is to deepen understanding of async programming in Python.

## Learning Objectives
By the end of this project, you should be able to:
- Write an asynchronous generator
- Use async comprehensions
- Type-annotate generators

## Requirements
- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 18.04 LTS using python3 (version 3.7)
- **Code Style**: Pycodestyle (version 2.5.x)
- **Documentation**: All modules, functions, and coroutines must have proper documentation explaining their purpose.
- **Type Annotations**: All functions and coroutines must be type-annotated.

## Tasks

### 0. Async Generator
Write a coroutine called `async_generator` that takes no arguments. It should:
- Loop 10 times, asynchronously waiting 1 second each time.
- Yield a random number between 0 and 10 using the `random` module.

**File**: `0-async_generator.py`

**Usage**:
```python
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
