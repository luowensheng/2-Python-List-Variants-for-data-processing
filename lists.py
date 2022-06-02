
from functools import reduce
from itertools import accumulate
from types import FunctionType
from typing import Any, List

class Stream(list):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def map(self, func):
        return Stream(map(func, iter(self)))
    
    def reduce(self, func):
        return reduce(func, iter(self))

    def accumulate(self, func):
        return Stream(accumulate(iter(self), func))
        
    def filter(self, func):
        return Stream(filter(func, iter(self))) 
    
    def foreach(self, func):
        for item in map(func, iter(self)): item
    

class LazyList(list):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.super__getitem__ :FunctionType[int, [Any]] = lambda i: args[0][i]
        self.__operations=[]
    
    def do(self, operation):
        self.__operations.append(operation)
        return self
    
    def clear(self):
        self.__operations = []
        return self
    
    def __getitem__(self, i):
       
        if isinstance(i, int):
           return reduce(lambda acc, f : f(acc), [self.super__getitem__(i) ]+self.__operations) 
       
        elif isinstance(i, slice):
            start = i.start or 0
            stop = len(self) if i.stop is None else i.stop if i.stop >0 else len(self)+i.stop
            step = i.step or 1
            return [self[j] for j in range(start, stop, step)]
        
        raise NotImplementedError()
            
    def collect(self, _filter=None):
        
        if _filter is None:
            return LazyList(self[:])
        
        else:
            return LazyList(self[:])