C, H = 50, 30
D = list(map(int, input().split(',')))
print(*([round((2*C*d/H)**0.5) for d in D]), sep=',') # use round() instead of int()