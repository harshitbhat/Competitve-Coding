N, H, x = map(int,input().split())
arr = list(map(int,input().split()))
if x + max(arr) >= H:
    print('YES')
else:
    print('NO')