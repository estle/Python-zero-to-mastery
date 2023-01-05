while True:
    try:
        n = int(input())
    except ValueError as err:
        print(err)
    else:
        break
d = {i: i*i for i in range(1, n+1)}
print(d)