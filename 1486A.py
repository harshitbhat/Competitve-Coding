T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    k = 0
    isPossible = True
    for i in range(0,len(arr) - 1):
        toGive = arr[i] - k
        arr[i+1] += toGive
        arr[i] = k
        k += 1
        if arr[i] >= arr[i+1]:
            isPossible = False
            break
    if isPossible:
        print('YES')
    else:
        print('NO')