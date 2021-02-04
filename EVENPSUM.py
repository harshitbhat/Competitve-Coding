t = int(input())
while t>0:
    t = t-1
    a,b = map(int,input().split())
    e1 = e2 = o1 = o2 = 0
    if a % 2 == 0:
        e1 = o1 = int(a/2)
    else:
        e1 = int(a/2)
        o1 = e1 + 1
    if b % 2 == 0:
        e2 = o2 = int(b/2)
    else:
        e2 = int(b/2)
        o2 = e2 + 1
    
    print((o1*o2) + (e1*e2))