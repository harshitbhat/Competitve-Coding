T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    lines = []
    for i in range(n):
        s = list(map(int,input().split()))
        lines.append(s[0])
        lines.append(s[1:len(s)])
    # Solving for n = 1
    ants = lines[1]
    ants.sort()
    negs = 0
    for i in ants:
        if i <= 0:
            negs += 1
        if i > 0:
            break
    pos = len(ants) - negs
    print(pos*negs)