t = int(input())
a,b = map(int,input().split())
t = t-1
cap = b - a
ans = cap
while t>0:
    t = t-1
    a,b = map(int,input().split())
    cap = cap - a
    cap = cap + b
    if ans < cap:
        ans = cap

print(ans)