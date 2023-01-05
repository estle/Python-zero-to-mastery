'''Solution by: yuan1z'''
func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)
a, b = input().split()
func(a, b)