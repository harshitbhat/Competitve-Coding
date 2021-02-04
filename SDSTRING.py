import math
T = int(input())
while T > 0:
    T = T - 1
    s = list(input())
    length = len(s)
    ans = 0
    if length % 2 != 0:
        ans = -1
    else:
        stk = []
        stk.append([s[0],0])
        top = s[0]
        for i in range(1,length):
            if top == -1:
                stk.append([s[i],i])
                top = s[i]
            elif top == s[i]:
                stk.append([s[i],i])
                top = s[i]
            else:
                stk.pop()
                if len(stk) == 0:
                    top = -1
                else:
                    top = stk[len(stk) - 1][0]
        i = len(stk) - 1
        # print(stk)
        while(i>=0):
            if s[stk[i][1] - 1] != stk[i][0]:
                ans = ans + 1
                stk.pop()
                stk.pop()
            i = i - 2
        if len(stk) != 0:
            ans = -1
    print(ans)




    4
    2 2 1
    2 3 10
    2 3 1
    5 6 20


    3
    2 2 1
    2 3 3
    2 3 1