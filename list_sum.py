def listSum(ls):
    if not ls:
        return 0
    
    return ls[0] + listSum(ls[1:])

print(listSum([1, 2, 3, 4, 5]))
