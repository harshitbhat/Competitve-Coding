k,n,w = map(int,input().split())
req = k * int((w*(w+1))/2)
if req > n:
    print(req-n)
else:
    print(0)