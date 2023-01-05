print(*(filter(lambda string: all(char in "02468" for char in string),\
    [str(x) for x in range(1000, 3001)])), sep=',')