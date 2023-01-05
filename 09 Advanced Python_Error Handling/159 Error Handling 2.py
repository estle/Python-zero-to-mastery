def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err: # handling multiple errors
        print(err) # variable that is 'TypeError'
        print(type(err))

sum('1', 2)