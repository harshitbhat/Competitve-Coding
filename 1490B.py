T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    c0 = 0
    c1 = 0
    c2 = 0
    for i in arr:
        if i % 3 == 0:
            c0 += 1
        elif i % 3 == 1:
            c1 += 1
        else:
            c2 += 1
    target = n // 3
    ans = 0
    if c0 < target:
        req = target - c0
        if c2 > target:
            if ((c2-target)-req) >= 0:
                ans += req
                c2 -= req
                c0 += req
                req = 0
            else:
                req -= (c2-target)
                ans += (c2-target)
                c0 += (c2-target)
                c2 = target
        if req != 0:
            if c1 > target:
                ans += 2*req
                c1 -= req
                c0 += req
                req = 0
    if c1 < target:
        req = target - c1
        if c0 > target:
            if ((c0-target)-req) >= 0:
                ans += req
                c0 -= req
                c1 += req
                req = 0
            else:
                req -= (c0 - target)
                ans += (c0 - target)
                c1 += (c0 - target)
                c0 = target
        if req != 0:
            if c2 > target:
                ans += 2*req
                c2 -= req
                c1 += req
                req = 0
    if c2 < target:
        req = target - c2
        if c1 > target:
            if ((c1-target)-req) >= 0:
                ans += req
                c1 -= req
                c2 += req
                req = 0
            else:
                req -= (c1-target)
                c2 += (c1-target)
                ans += (c1-target)
                c1 = target 
        if req != 0:
            if c0 > target:
                ans += 2*req
                c0 -= req
                c2 += req
                req = 0
    print(ans)