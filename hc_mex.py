import math
T =int(input())
while T > 0:
    T = T -1
    n = int(input())
    arr =list(map(int,input().split()))
    temp = []
    for i in range(0,n):
        for j in range(i+1,n):
            temp.append(math.gcd(arr[i],arr[j]))
    i = 1
    while True:
        if i in temp:
            i += 1
        else:
            break
    print(i)