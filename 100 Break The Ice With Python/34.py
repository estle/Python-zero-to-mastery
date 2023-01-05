def printList():
    lst = [i**2 for i in range(1, 21)]
    print(*lst[:5])

printList()