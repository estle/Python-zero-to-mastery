# lambda expresssions Keep it nice & clean
# useful when using a function only once
lambda param: action(param)
my_list = [1, 2, 3]
print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
from functools import reduce
print(reduce(lambda acc, item: acc+item, my_list))
# One-line functions