# Higher Order Function (HOF)
def greet(func): # Func that accepts as parameter another function
    func()

def greet2():
    def func():
        return 5
    return func # HOF returns another Func
# map, filter, reduce – are all HOF