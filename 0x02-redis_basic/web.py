#!/usr/bin/env python3
"""
Redis class testing
"""

import requests
import redis
from typing import Callable
from functools import wraps

cache = redis.Redis()


def cache_url(method: Callable):
    """
    Cache url wrapper
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """
        wrapper function
        """
        cache.hincrby(f'count:{args[0]}', args[0], 1)
        out = requests.get(args[0])
        cache.set(args[0], out.text)
        cache.expire(args[0], 10)
        return out
    return wrapper


@cache_url
def get_page(url: str) -> str:
    """Uses requests to get HTML content of url
    """
    pass


get_page('https://google.com')
