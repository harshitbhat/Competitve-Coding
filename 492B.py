n,l = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
minRad = 0
for i in range(0,n-1):
    if (arr[i+1] - arr[i]) > minRad:
        minRad = arr[i+1] - arr[i]
minRad = minRad/2
if arr[0] != 0:
    if minRad < arr[0]:
        minRad = arr[0]
if arr[n-1] != l:
    if minRad < (l - arr[n-1]):
        minRad = l - arr[n-1]
print('%.10f'%minRad)
