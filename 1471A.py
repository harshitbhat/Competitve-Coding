import math
T = int(input())
while T > 0:
    T = T - 1
    n , x = map(int,input().split())
    a =list(map(int,input().split()))
    s = 0
    temp = 0
    for i in a:
        s += i
        temp += math.ceil(i/x)
    print(min(temp,math.ceil(s/x)),max(temp,math.ceil(s/x)))