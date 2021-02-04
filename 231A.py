t = int(input())
ans = 0
while t>0:
    t = t-1
    st = input()
    arr =[]
    arr= list(map(int,st.split()))
    ct = 0
    for i in arr:
        if i == 1:
            ct = ct+1
    if ct > 1:
        ans = ans+1
print(ans)
