li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i<1 or i>3]
print(li)