n = int(input())
arr = list(map(int,input().split()))
s = 0
for i in arr:
    s += i
print('{:.12f}'.format(s/n))