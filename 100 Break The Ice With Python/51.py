def func():
    return 5/0
    
try:
    func()
except ZeroDivisionError:
    print('cannot divide by zero')
except:
    print('other exception')