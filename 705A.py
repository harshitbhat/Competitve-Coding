n = int(input())
i = 1
while i<=n-1:
    if i%2 == 0:
        print('I love that',end=' ')
    else:
        print('I hate that',end=' ')
    i = i + 1
if n % 2 == 0:
    print('I love it')
else:
    print('I hate it')