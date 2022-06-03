# 2 Python List Variants for data processing

1. ## LazyList

 The LazyList doesn't perform any operations until an item is requested. Instead, it stores the operations in list. It allows to perform multiple operations, similar to a functional programming style like Haskell.

```python

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
            
    def collect(self):
            return LazyList(self[:])
            
```
### Usage 

```python
    items = [2,5,6,8,9,0]
    lazy_list = LazyList(items)     
    
    print (
        lazy_list.do(lambda x: x*3)
        .do(lambda x: x+3)
        .do(lambda x: x/4)
        .do(lambda x: f"the final result is ({x})")
        [0]
    )

```

### Output 

```
the final result is (2.25)
```




2. ## Stream

 Similar to Streams in java. It allows performing map, filter, reduce and foreach on a list.

```python 
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
    
```

### Usage

```python 
    items = [2,5,6,8,9,0]
    stream = Stream(items)
    print(
        stream.map(lambda x: x+2)
        .filter(lambda x: x>4)
        .accumulate(lambda x, y: x+y)
        .reduce(lambda x, y: x+y)
    )
```

### Output

```
83
```