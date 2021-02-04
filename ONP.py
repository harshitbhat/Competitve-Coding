t = int(input())
while t > 0:
    t = t - 1
    s = input()
    ans = []
    stk = []
    for i in s:
        if i == '(' or i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
            stk.append(i)
        elif i == ')':
            while True:
                temp = stk.pop()
                if temp == '(':
                    break
                ans.append(temp)
        else:
            ans.append(i)
    for i in ans:
        print(i,end="")
    print()