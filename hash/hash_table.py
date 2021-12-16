from typing import Any

SIZE = 256


def hash(k: int) -> int:
    return k % SIZE  # just a simple hash :)


class HashTable:
    def __init__(self) -> None:
        self._data = [list() for _ in range(SIZE)]

    def add(self, key: int, value: Any):
        self._data[hash(key)].append((key, value))

    def get(self, key: int) -> Any:
        for index, (f_key, f_value) in enumerate(self._data[hash(key)]):
            if f_key == key:
                self._data[hash(key)].pop(index)
                return f_value
        raise KeyError(key)
