import math
T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = []
    for i in range(n):
        l,r,z = map(int,input().split())
        arr.append([r,z])
    arr.sort()
    w = 1
    delivered = 0
    for i in arr:
        req = i[1]
        if ((w * i[0]) - delivered) < req:
            w = math.ceil((req + delivered)/i[0])
        delivered += req
    print(w)

