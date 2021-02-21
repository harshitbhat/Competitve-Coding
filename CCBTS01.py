# cook your dish here
import math
T = int(input())
while T > 0:
    T = T - 1
    s = input()
    if 'P' in s and 'C' in s and 'M' in s:
        print('YES')
    else:
        print('NO')