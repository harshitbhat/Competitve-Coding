n = input()
arr = list(map(int,input().split()))
count = {
    1:0,
    2:0,
    3:0,
    4:0
}

for i in arr:
    count[i] = count[i] + 1

ans = count[4]

if count[1] <= count[3]:
    ans = ans + count[3]
    count[1] = 0
else:
    ans = ans + count[3]
    count[1] = count[1] - count[3]

if count[2]%2 == 0:
    ans = ans + int(count[2]/2)
else:
    ans = ans + int(count[2]/2) + 1
    if count[1] > 2:
        count[1] = count[1] - 2
    else:
        count[1] = 0

if count[1] > 0:
    if count[1] > 4:
        if count[1] % 4 == 0:
            ans = ans + int(count[1]/4)
        else:
            ans = ans + int(count[1]/4) + 1
    else:
        ans = ans + 1

print(ans)