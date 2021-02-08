T = int(input())
while T > 0:
    T = T - 1
    s = input()
    ans = []
    for i in range(0,len(s)):
        if i % 2 == 0:
            if s[i] == 'a':
                ans.append('b')
            else:
                ans.append('a')
        else:
            if s[i] == 'z':
                ans.append('y')
            else:
                ans.append('z')
    for i in ans:
        print(i,end="")
    print()