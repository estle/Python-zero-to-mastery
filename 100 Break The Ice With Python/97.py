n = 4 # n*2-1
s = ''
ans = []
for char in range(ord('a')+n-1, ord('a')-1, -1):
    x = s
    s += chr(char)
    p = x+s[-1]+x[::-1]
    ans.append(p)
x = ans[:-1]
ans += x[::-1]
for line in ans:
    add = (n*4-2-(2*len(line)-1))//2
    print(add*'-', end='')
    print(*[c for c in line], sep='-', end='')
    print(add*'-')