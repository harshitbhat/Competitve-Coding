T = int(input())
while T > 0:
    T = T - 1
    n , k = map(int,input().split())
    arr = list(map(int,input().split()))
    hash = [0] * n
    i = n-2
    countStored = 0
    while i >= 0:
        if arr[i] < arr[i+1] + hash[i+1]:
            hash[i] = (arr[i+1] + hash[i+1]) - arr[i]
            countStored += hash[i]
        i -= 1
    print(hash)
    if k > countStored:
        print(-1)
    else:
        ind = 0
        for j in range(0,k):
            for i in range(0,n-1):
                if arr[i] < arr[i+1]:
                    arr[i] += 1
                    ind = i
                    break
        print(i+1)
     