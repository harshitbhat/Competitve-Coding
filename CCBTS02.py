# cook your dish here
import math
T = int(input())
while T > 0:
    T = T - 1
    n  = int(input())
    arr = list(input().split())
    current = 0
    error = False
    for i in arr:
        if i == 'start' or i == 'restart':
            if current == 0:
                current = 1
        else:
            if current == 1:
                current = 0
            else:
                error = True
                break
    if error:
        print(404)
    else:
        print(200)
