def gen(x):
    for i in range(x+1):
        if i%35==0:
            yield i

print(*[d for d in gen(int(input()))], sep=',')