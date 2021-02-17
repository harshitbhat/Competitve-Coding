n = int(input())
s = input()
s = s.lower()
if len(set(s)) != 26:
    print('NO')
else:
    print('YES')