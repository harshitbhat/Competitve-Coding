n,k = map(int,input().split())
s = input()
arr = []
for i in s:
    arr.append(i)
while k > 0:
    k = k - 1
    change = []
    for i in range(0,n-1):
        if arr[i] == 'B' and arr[i+1] == 'G':
            change.append(i)
    for i in change:
        arr[i] = 'G'
        arr[i+1] = 'B'
for i in range(0,n):
    print(arr[i],end='')
print('')