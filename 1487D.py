import math
fill = []
def preFill():
    for i in range(3,10**5,2):
        x = i**2
        a = i
        b = ((a**2) - 1) // 2
        c = b + 1
        fill.append(c)
def solve(n):
    low = 0
    high = len(fill) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if fill[mid] <= n:
            low = mid+1
        else:
            ans = mid
            high = mid - 1
    return ans


T = int(input())
preFill()
while T > 0:
    T = T - 1
    n = int(input())
    print(solve(n))