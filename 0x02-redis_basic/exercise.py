#!/usr/bin/env python3
""" Module definition """

import redis
from typing import Union
import uuid


class Cache:
    """ Cache class """
    def __init__(self):
        """ Initilaization method for Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores input data using a random key and returns key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
