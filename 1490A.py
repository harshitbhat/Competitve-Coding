import math
def check(a,b):
    return (max(a,b) / min(a,b)) <= 2
T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    original = len(arr)
    i = 0
    while i < len(arr) - 1:
        if check(arr[i],arr[i+1]):
            i += 1
        else:
            if arr[i+1] > arr[i]:
                arr.insert(i+1,2*arr[i])
            else:
                arr.insert(i+1, math.ceil(arr[i]/2))
    print(len(arr) - original)