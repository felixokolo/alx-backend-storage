#!/usr/bin/env python3
"""
Redis class testing
"""
import redis
from uuid import uuid4
from typing import Union
from typing import Callable
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """
    Decorator function
    """

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function
        """
        self._redis.incrby(fn.__qualname__, 1)
        return fn(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    Redis cache class definition
    """

    def __init__(self) -> None:
        """
        Init method for cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: bytes) -> str:
        """
        Stores data using random uuid key

        Parameters:
        data (bytes): Bytes data to store

        Returns:
        UUID key of stored data
        """

        k = str(uuid4())
        self._redis.mset({k: data})
        return k

    def get(self, key: Union[bytes, str],
            fn: Callable = None) -> Union[bytes, int, str, float, None]:
        """
        Get a key from redis database
        """

        ret: Union[bytes,
                   int,
                   str,
                   float,
                   None] = self._redis.get(key)
        if ret is None or fn is None:
            return ret
        return fn(ret)

    def get_str(self, key: Union[bytes, str]):
        """
        gets a str from redis database
        """

        return self.get(key, str)

    def get_int(self, key: Union[bytes, str]):
        """
        gets an int from redis database
        """

        return self.get(key, int)
