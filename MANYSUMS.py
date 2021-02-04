T = int(input())
while T > 0:
    T = T - 1
    a,b = map(int,input().split())
    print(2*b - 2*a + 1)