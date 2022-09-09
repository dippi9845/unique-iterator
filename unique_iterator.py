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

if __name__ == "__main__":
    from random import randint
    '''
    Works for already unique values
    
    a = [1,2,3,4,5,6]
    
    for i in UniqueIterator(a):
        print(i)
    input()
    '''
    
    '''
    
    Works with duplicated values
    is something uncreased by 30% - 75%
    
    from time import time
    s = time()
    values = [randint(1,6) for i in range(10_000_000)]
    e = time()
    print("creation took", e-s)
    
    s = time()
    for i in values:
        pass
    e = time()
    print("normal looping took", e-s)
    
    s = time()
    for i in UniqueIterator(values):
        print(i)
    e = time()
    print("unique looping took", e-s)
    input()
    
    '''
    
    '''
    Works with objects that are overrided equals and hash
    
    class Pearson:
        def __init__(self, name: str, surname: str, age : int) -> None:
            self.name = name
            self.surname = surname
            self.age = age
        
        def __eq__(self, __o: object) -> bool:
            return __o.name == self.name and __o.surname == self.surname and __o.age == self.age
        
        def __hash__(self) -> int:
            return hash(hash(self.surname) + hash(self.name) + hash(self.age))
        
        def __str__(self) -> str:
            return self.name + " " + self.surname + " " + str(self.age)
    
    a = [Pearson("sjdhfaj", "sfdhgjd", 11), Pearson("sjdgfaj", "sfdhgjd", 11), Pearson("sjfdgj", "sfdhfdgjd", 11), Pearson("sjdhfaj", "sfdhgjd", 11)]
    
    for i in UniqueIterator(a):
        print(i)
    
    '''