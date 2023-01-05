from math import sqrt
d1, d2 = 0, 0
while 1:
    s = input().split()
    if not s: break
    if s[0]=='UP': d1 += int(s[1])
    elif s[0]=='DOWN': d1 -= int(s[1])
    elif s[0]=='LEFT': d2 += int(s[1])
    elif s[0]=='RIGHT': d2 -= int(s[1])
print(round(sqrt(d1**2+d2**2)))
    