import itertools

lst = [1,2,3]
print(*list(itertools.permutations(lst)), sep='\n')