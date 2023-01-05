def for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break
        
        
for_loop([1,2,3])

print()

class MyGen():
    def __init__(self, first, last):
        self.first, self.current = first, first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.last:
            c = self.current
            self.current += 1
            return c
        raise StopIteration
    
    
g = MyGen(90, 100)
for i in g:
    print(i, end=' ')