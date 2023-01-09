def bsearch(x):
    l,r=0,len(lst)-1
    while l<r:
        mid = (l+r)//2
        if lst[mid]<x:
            l = mid+1
        else:
            r = mid
    if lst[r]==x:
        return l
    return "no such element"

lst = [1,3,4,9,22]
print(bsearch(4))