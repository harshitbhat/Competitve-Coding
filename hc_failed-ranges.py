n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x , y = map(int,input().split())
temp = []
for i in range(0,n):
    for j in range(0,m):
        temp.append([a[i] + b[j],i,j])
temp.sort()
ans = []
for i in temp:
    if i[0] > temp[x-1][0] and i[0] < temp[y-1][0]:
        ans.append(i)

print(len(ans))
for i in ans:
    print('(' + str(i[1] + 1) + ',' + str(i[2] + 1) + ') ',end='')
print()
