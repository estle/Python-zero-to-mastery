s = "abcdefgabc"
d = {i:s.count(i) for i in s}
print(*[f'{i[0]},{i[1]}' for i in d.items()], sep='\n')