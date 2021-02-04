d1,v1,d2,v2,p = map(int,input().split())
day = 0
ans = 0
while ans < p:
    day = day + 1
    if d1 <= day:
        ans = ans + v1
    if d2 <= day:
        ans = ans + v2
print(day)