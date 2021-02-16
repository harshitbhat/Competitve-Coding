T = int(input())
while T > 0:
    T = T - 1
    a, b = map(int,input().split())
    if a % b == 0:
        print(0)
    else:
        print(b - a%b)