def fact(num):
    res = 1
    for i in range(1, num+1):
        res *= i
        if i in x: dt[i] = res


x = list(map(int, input().split()))
dt = {0:1}
fact(max(x))
print(*([dt[i] for i in x]), sep=',')
