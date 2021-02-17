check = {}
check['Tetrahedron'] = 4
check['Cube'] = 6
check['Octahedron'] = 8
check['Dodecahedron'] = 12
check['Icosahedron'] = 20

n = int(input())
ans = 0
for i in range(n):
    t = input()
    ans += check[t]
print(ans)