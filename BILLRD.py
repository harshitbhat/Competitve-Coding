T = int(input())
while T > 0:
    T = T - 1
    n,k,x,y = map(int,input().split())
    ansx = -1
    ansy = -1
    k = k % 4
    if x == y:
        ansx = ansy = n
    elif  x > y:
        lowerTriangle = {
            0 : [x-y,0],
            1 : [n,n+(y-x)],
            2 : [n+(y-x),n],
            3 : [0,x-y]
        }
        ansx = lowerTriangle[k][0]
        ansy = lowerTriangle[k][1]
    else:
        upperTriangle = {
            0 : [0,y-x],
            1 : [n+(x-y),n],
            2 : [n,n+(x-y)],
            3 : [y-x,0]
        }
        ansx = upperTriangle[k][0]
        ansy = upperTriangle[k][1]
    print(f"{ansx} {ansy}")
        