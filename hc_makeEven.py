T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    i = 0
    ans = 0
    while i< n-1:
        if arr[i] % 2 == 0:
            i+=1
        if arr[i] % 2 != 0 and arr[i+1] % 2 != 0:
            ans += 1
            i += 2
        elif (arr[i] % 2 == 0 and arr[i+1] % 2 != 0 ) or (arr[i] % 2 != 0 and arr[i+1] % 2 == 0):
            ans += 2
            i += 2
    print(ans)