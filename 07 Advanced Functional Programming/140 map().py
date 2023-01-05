# the idea of pure functions with all functionality inside
def multiply_by2(item):
    return item*2


my_list = [1, 2, 3] # using map as a functional programming paradigm to quickly iterate through elems
print(list(map(multiply_by2, my_list))) # map(action, data)
print(my_list)