# map filter zip reduce
from functools import reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item


my_list = [1, 2, 3]
print(reduce(accumulator, my_list, 10))