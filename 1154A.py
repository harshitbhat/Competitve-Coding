c = list(map(int,input().split()))
c.sort()
print(f"{c[3]-c[2]} {c[3]-c[1]} {c[3]-c[0]}")