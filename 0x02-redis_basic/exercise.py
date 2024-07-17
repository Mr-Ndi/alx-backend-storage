#!/usr/bin/env pyhon3

import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to a method using Redis."""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
            Increment the call count for the
            method and call the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->
    Union[str, bytes, int, float, None]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        value = self.get(key, fn=lambda x: x.decode('utf-8'))
        return value

    def get_int(self, key: str) -> Optional[int]:
        value = self.get(key, fn=int)
        return value


if __name__ == "__main__":
    cache = Cache()

    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))
