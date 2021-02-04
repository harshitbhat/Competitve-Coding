t = int(input())
while t>0:
    t = t-1
    n,d = map(int,input().split())
    arr = list(map(int,input().split()))
    if d == 1:
        print(n)
    else:
        risk = 0
        for i in arr:
            if i <= 9 or i >= 80:
                risk = risk + 1
        ans = 0
        if risk % d == 0:
            ans = int(risk/d)
        else:
            ans = int(risk/d) + 1
        notAtRisk = n-risk
        if notAtRisk % d == 0:
            ans = ans + int(notAtRisk/d)
        else:
            ans = ans + int(notAtRisk/d) + 1
        print(ans)