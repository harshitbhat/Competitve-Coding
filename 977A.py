n,k = map(int,input().split())
while k > 0:
    k = k-1
    if n % 10 == 0:
        n = int(n/10)
    else:
        n = n - 1
print(n)