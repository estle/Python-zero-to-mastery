def inputs():
    while True:
        s = input()
        if not s:
            return
        yield s
        

print(*(line.upper() for line in inputs()), sep='\n')
# My Elegant Solution Using Advanced Python Generators