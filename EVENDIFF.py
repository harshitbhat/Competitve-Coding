T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    odd = 0
    even = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(min(odd,even))