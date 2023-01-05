C, H = 50, 30
D = list(map(int, input().split(',')))
print(*([int((2*C*d/H)**0.5) for d in D]), sep=',')