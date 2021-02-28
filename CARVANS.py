T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 1
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            arr[i] = arr[i-1]
        else:
            ans += 1
    print(ans) 