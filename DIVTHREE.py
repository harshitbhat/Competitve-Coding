T = int(input())
while T > 0:
    T = T - 1
    n,k,d = map(int,input().split())
    arr = list(map(int,input().split()))
    totalProbs = 0
    for i in arr:
        totalProbs += i
    noOfDays = totalProbs // k
    print(min(d,noOfDays))