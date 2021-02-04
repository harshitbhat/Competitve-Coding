def diff(a,b):
    if a>b:
        return a-b
    else:
        return b-a

arr = []
for i in range (0,5):
    s = list(map(int,input().split()))
    arr.append(s)
x = 0
y = 0

for i in range(0,5):
    a = arr[i]
    for j in range(0,5):
        if a[j] == 1:
            x = i+1
            y = j+1
            break

print(diff(x,3) + diff(y,3))
