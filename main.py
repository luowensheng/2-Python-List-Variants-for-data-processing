from lists import Stream, LazyList

                  
def try_lazy_list(items):        
        
    lazy_list = LazyList(items)     
    
    print (
        lazy_list.do(lambda x: x*3)
        .do(lambda x: x+3)
        .do(lambda x: x/4)
        .do(lambda x: f"the final result is ({x})")
        [0]
    )



def try_stream(items):

    stream = Stream(items)

    print(
        stream.map(lambda x: x+2)
        .filter(lambda x: x>4)
        .accumulate(lambda x, y: x+y)
        .reduce(lambda x, y: x+y)
    )
    
if __name__ == '__main__':
    
    items = [2,5,6,8,9,0]
    
    try_lazy_list(items)    
    try_stream(items)    