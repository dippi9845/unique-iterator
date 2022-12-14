from typing import Iterable

class Unique:
    '''
    This class model an Iterator that is built from another Iterator,
    and returns only uniques value that the iterator provided, supllies.
    '''
    
    def __init__(self, iterable : Iterable[object]) -> None:
        '''
        For build an Unique iterator you need to provide a iterator which
        returns objects that supports __eq__ and __hash__
        '''
        self.iterable = iter(iterable)
        self.values = set()
    
    def __iter__(self):
        '''
        Return himself couse it suports next
        '''
        return self
    
    def __next__(self) -> object:
        '''
        Return the next unique element that the iterator provided supplies
        '''
        value = next(self.iterable)
        
        while value in self.values:
            value = next(self.iterable)
        
        self.values.add(value)
        return value
