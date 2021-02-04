def countKey(arr,key):
    sum = 0
    for i in arr:
        if i == key:
            sum = sum + 1
    return sum

T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    pS = input()
    qS = input()
    p = []
    p [:0] = pS
    q = []
    q [:0] = qS
    z1 = countKey(p,'0')
    o1 = countKey(p,'1')
    z2 = countKey(q,'0')
    o2 = countKey(q,'1')
    if z1 == z2 and o1 == o2:
        i = 0
        while i < n:
            if p[i] != q[i] and p[i] == '1':
                for j in range(i,n):
                    if p[j] == q[i]:
                        temp = p[i]
                        p[i] = p[j]
                        p[j] = temp
                        break
            i = i + 1
        if p == q:
            print('Yes')
        else:
            print('No')
    else:
        print('No')