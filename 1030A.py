n = int(input())
arr = list(map(int,input().split()))
has = False
for i in arr:
    if i == 1:
        has = True
if has == True:
    print('HARD')
else:
    print('EASY')