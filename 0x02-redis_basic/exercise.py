#!/usr/bin/env python3
"""
Redis class testing
"""
import redis
from uuid import uuid4
from typing import Union
from typing import Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator function
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator function
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function
        """
        inkey = f'{method.__qualname__}:inputs'
        outkey = f'{method.__qualname__}:outputs'
        out = method(self, *args, **kwargs)
        self._redis.rpush(inkey, str(args))
        self._redis.rpush(outkey, out)
        return out

    return wrapper


class Cache:
    """Cache.store was called 3 times:
    Redis cache class definition
    """

    def __init__(self) -> None:
        """
        Init method for cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[bytes,
                                str,
                                int,
                                float]) -> str:
        """
        Stores data using random uuid key

        Parameters:
        data (bytes): Bytes data to store

        Returns:
        UUID key of stored data
        """

        k: str = str(uuid4())
        if data is None or type(data) not in [bytes,
                                              str,
                                              int,
                                              float]:
            return k
        self._redis.set(k, data)
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


def replay(fn: Callable) -> None:
    """
    Prints a formatted out put of calls details of fn
    """

    cache = redis.Redis()
    print(f'{fn.__qualname__}' +
          f' was called {cache.get(fn.__qualname__).decode("utf-8")} times:')
    inputs = cache.lrange(f'{fn.__qualname__}:inputs', 0, -1)
    outputs = cache.lrange(f'{fn.__qualname__}:outputs', 0, -1)
    for ins, outs in zip(inputs, outputs):
        print(f"{fn.__qualname__}" +
              f"(*{ins.decode('utf-8')}) -> {outs.decode('utf-8')}")
