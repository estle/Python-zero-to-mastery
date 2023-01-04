def fib(number): # argument is index number
    f0, f1 = 0, 1
    for i in range(number):
        yield f0
        f0, f1 = f1, f0+f1


for i in fib(1):
    print(i)
print("hello"[0])