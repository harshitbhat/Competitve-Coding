T = int(input())
while T > 0:
    T -= 1
    credentials = input().split()
    n = int(credentials[0])
    origin  = credentials[1]
    points = 0
    for i in range(n):
        s = input()
        s = s.split()
        if s[0] == 'CONTEST_WON':
            rank = int(s[1])
            if rank < 20:
                points += 300 + (20 - rank)
            else:
                points += 300
        if s[0] == 'TOP_CONTRIBUTOR':
            points += 300
        if s[0] == 'BUG_FOUND':
            points += int(s[1])
        if s[0] == 'CONTEST_HOSTED':
            points += 50
    if origin == 'INDIAN':
        print(points // 200)
    else:
        print(points // 400)