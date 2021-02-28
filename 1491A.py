n , q = map(int,input().split())
arr = list(map(int,input().split()))
count0 = arr.count(0)
count1 = arr.count(1)
for i in range(q):
    x , y = map(int,input().split())
    if x == 1:
        if arr[y-1] == 0:
            arr[y-1] = 1
            count0 -= 1
            count1 += 1
        else:
            arr[y-1] = 0
            count1 -= 1
            count0 += 1
    else:
        if y <= count1:
            print(1)
        else:
            print(0)
        