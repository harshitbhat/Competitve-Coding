'''
February Challenge 2021 Division 2
Question: https://www.codechef.com/FEB21B/problems/MAXFUN
'''
T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    print(abs(arr[n-1] - arr[0]) + abs(arr[n-1] - arr[1]) + abs(arr[1] - arr[0]))
