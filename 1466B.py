T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    myHash = {}
    for i in arr:
        myHash[i] = 0
    for i in arr:
        myHash[i] = myHash[i] + 1
    keyArr = list(myHash.keys())
    for i in keyArr:
        if myHash[i] > 1:
            if (i + 1) in myHash.keys():
                myHash[i + 1] = myHash[i + 1] + 1
            else:
                myHash[i + 1] = 1
    print(len(myHash))
