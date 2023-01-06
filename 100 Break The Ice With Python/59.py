n = int(input())
print(f'{sum(i/(i+1) for i in range(1, n+1)):.2f}')