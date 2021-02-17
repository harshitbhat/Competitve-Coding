n , m = map(int,input().split())
ct = 0
while n and m:
    n -= 1
    m -= 1
    ct += 1
if ct % 2 == 0:
    print('Malvika')
else:
    print('Akshat')