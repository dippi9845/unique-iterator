from random import randint
from typing import Iterable

class UniqueIterator:
    def __init__(self, iterable : Iterable[object]) -> None:
        self.iterable = iterable
        self.values = set()
    
    def __iter__(self):
        return self
    
    def __next__(self) -> object:
        value = next(x for x in self.iterable if not x in self.values)
        self.values.add(value)
        return value
