def f(n):
    if ans[n]!=-1:
        return ans[n]
    ans[n] = f(n-1)+f(n-2)
    return ans[n]

n = int(input())
ans = [-1]*(n+1)
ans[0], ans[1] = 0, 1
f(n)
print(*ans, sep=',')