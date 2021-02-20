n = int(input())
ms = 0
cs = 0
for i in range(n):
    m,c = map(int,input().split())
    if m > c:
        ms += 1
    elif m < c:
        cs += 1
    else:
        ms += 1
        cs += 1
if ms > cs:
    print('Mishka')
elif ms < cs:
    print('Chris')
else:
    print('Friendship is magic!^^')