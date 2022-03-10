def printN(n):
    if n == 0:
        return 0
    
    print(n)
    return printN(n-1)

print(printN(5)) # 5 4 3 2 1 0