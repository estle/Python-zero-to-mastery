lst = []
while 1:
    s = input()
    if not s:
        break
    lst.append(tuple(s.split(',')))
lst.sort(key=lambda x:[x[0],int(x[1]),int(x[2])]) # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
print(lst)