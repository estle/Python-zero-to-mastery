# map filter zip reduce
# the idea of pure functions with all functionality inside
def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0

my_list = [1, 2, 3]
print(list(filter(only_odd, my_list)))
print(my_list)

# Everything is nice and easy with map() and filter() functions