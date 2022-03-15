jumps = {}

n = int(input())

for i in range(n):
    steps = list(map(int, input().split()))
    jumps[steps[0]] = steps[1]

m = int(input())

plays = list(map(int, input().split()))

a = b = 0

for i in range(m):
    if i % 2 == 0:
        a += plays[i]
        while a in jumps.keys():
            a = jumps[a]

    else:
        b += plays[i]
        while b in jumps.keys():
            b = jumps[b]

if a > b:
    print(f'A {a}')
else:
    print(f'B {b}')

