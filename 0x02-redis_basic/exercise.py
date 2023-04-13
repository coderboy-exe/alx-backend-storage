#!/usr/bin/env python3
""" Module definition """

import redis
from typing import Union, Optional, Callable
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts houw many times methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper for decorator function count_calls"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper for decoration function call_history"""
        data = str(args)
        self._redis.rpush(key + ":inputs", data)
        output = method(self, *args, **kwargs)
        self._redis.rpush(key + ":outputs", output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    key = method.__qualname__
    redis = method.__self__._redis
    inputs = redis.lrange(key + ":inputs", 0, -1)
    outputs = redis.lrange(key + ":outputs", 0, -1)

    print(f"{key} was called {len(outputs)} times:")
    for k, v in zip(inputs, outputs):
        k = k.decode("utf-8")
        v = v.decode("utf-8")
        print(f"{key}(*{k}) -> {v}")


class Cache:
    """ Cache class """
    def __init__(self):
        """ Initilaization method for Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores input data using a random key and returns key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """converts key (if exists) from byte-string back to format"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """ parametrize stored data(key) to string """
        return self.get(key, str)

    def get_int(self, key: int) -> Union[int, None]:
        """ parametrize stored data(key) to int """
        return self.get(key, int)
