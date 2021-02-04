MAX = 1000005
possible = [False] * MAX
for i in range(0,1000):
    for j in range(0,1000):
        s = i * 2020 + j * 2021
        if s < MAX:
            possible[s] = True

T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    if possible[n] == True:
        print('YES')
    else:
        print('NO')