def generator_func(n):
    for i in range(n):
        yield i
        
        
g = generator_func(100)
print(g)
next(g) # 0
next(g) # 1
print(next(g)) # 2
next(g) # 3
    
# def make_list(num):
#     result = []
#     for i in range(num): # Generator is not held in memory
#         result += [i*2]
#     return result