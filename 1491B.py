import sys
T = int(input())
while T > 0:
    T -= 1
    n, u, v = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = sys.maxsize
    if n == 2:
        if abs(arr[0] - arr[1]) == 0:
            ans = min(u + v, 2 * v)
        elif abs(arr[0] - arr[1]) == 1:
            ans = min(u,v)
        else:
            ans = 0 
    else:
        isPossible = False
        isOne = False
        for i in range(1,n):
            if abs(arr[i] - arr[i-1]) > 1:
                isPossible = True
                break
            if abs(arr[i] - arr[i-1]) == 1:
                isOne = True
        if isPossible:
            ans = 0
        else:
            if isOne:
                ans = min(u,v)
            else:
                ans = min(u + v, 2 * v)
    print(ans)