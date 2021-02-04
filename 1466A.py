def calcArea(x1,y1,x2,y2,x3,y3):
    return (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2

T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    fixedx = 0
    fixedy = 1
    diffArea = {}
    for i in range(0,n):
        for j in range(i+1,n):
            area = calcArea(arr[i],0,arr[j],0,fixedx,fixedy)
            diffArea[area] = 1
    print(len(diffArea))
    