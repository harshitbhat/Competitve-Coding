
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

check = [False] * (d + 1)

for i in range(k,d+1,k):
    check[i] = True
for i in range(l,d+1,l):
    check[i] = True
for i in range(m,d+1,m):
    check[i] = True
for i in range(n,d+1,n):
    check[i] = True
ans = 0
for i in range(1,d+1):
    if check[i] == True:
        ans += 1
print(ans)