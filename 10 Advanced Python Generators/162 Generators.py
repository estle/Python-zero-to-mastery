range(100) # is a generator – special type
def make_list(num):
    result = []
    for i in range(num): # Generator is not held in memory
        result += [i*2]
    return result

my_list = make_list(20000000) # we wait till list takes up the space and creates, range does not need that
print('done')
    