ans = []
while True:
    s = input()
    if s: ans.append(s.upper())
    else: break
print(*ans, sep='\n')