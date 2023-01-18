#!/usr/bin/env python3
"""
Redis class testing
"""
import redis
from uuid import uuid4


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
