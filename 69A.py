t = int(input())
vectors = []
for i in range(0,t):
    z = list(map(int,input().split()))
    vectors.append(z)
ans = [0,0,0]
for i in range(0,t):
    ans[0] = ans[0] + vectors[i][0]
    ans[1] = ans[1] + vectors[i][1]
    ans[2] = ans[2] + vectors[i][2]

if ans[0] == 0 and ans[1] == 0 and ans[2] == 0:
    print('YES')
else:
    print('NO')