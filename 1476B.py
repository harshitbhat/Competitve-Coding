import math
T = int(input())
while T > 0:
    T = T - 1
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    prefix = []
    prefix.append(a[0])
    for i in range(1,n):
        prefix.append(prefix[i-1] + a[i])
    addition = 0
    for i in range(1,n):
        inflation = (a[i]/prefix[i-1]) * 100
        if inflation > k:
            toAdd = math.ceil((a[i] * 100)/ k) - prefix[i-1]
            addition += toAdd
            for j in range(i,n):
                prefix[j] += toAdd
    print(addition)