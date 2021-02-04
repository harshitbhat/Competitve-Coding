T = int(input())
while T > 0:
    T = T - 1
    n,c01,c10 = map(int,input().split())
    arr = list(map(int,input().split()))
    ans1 = ans2 = 0
    arr1 = [0] * n
    arr2 = [1] * n
    for i in range(1,n,2):
        arr1[i] = 1
        arr2[i] = 0
    for i in range(0,n):
        if arr[i] != arr1[i]:
            if arr[i] == 0:
                ans1 += c01
            else:
                ans1 += c10
        if arr[i] != arr2[i]:
            if arr[i] == 0:
                ans2 += c01
            else:
                ans2 += c10
    if ans1 < ans2:
        print(ans1)
    else:
        print(ans2)
