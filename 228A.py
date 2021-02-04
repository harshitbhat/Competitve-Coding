a,b,c,d = map(int,input().split())
check = {}
check[a] = True
check[b] = True
check[c] = True
check[d] = True

print(4- len(check))
