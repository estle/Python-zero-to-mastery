# Real-world applications of Decorators
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} sec')
        return result
    return wrapper

@performance
def long_time():
    flag = False
    for i in range(int(10**7)):
        flag ^= True

long_time()
