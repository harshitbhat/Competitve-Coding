T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ct1 = arr.count(arr[0])
    if ct1 == n:
        print(0)
    else:
        print(n-ct1)
        