def hello():
    print('hellooo')
    
def bye(func):
    func()
    
greet = hello
del hello # deletes the name, not the function

print(greet()) # greet prints 'hellooo' and returns None
bye(greet) # prints 'hellooo'
# @decorators are only available because we can call functions as variables