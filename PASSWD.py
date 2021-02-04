T = int(input())
while T > 0:
    T = T - 1
    s = input()
    isValid = True
    if len(s) >=10:
        hasLower = False
        for i in s:
            if i.islower() == True:
                hasLower = True
                break
        if hasLower == True:
            hasUpper = False
            for i in range(0,len(s)):
                if s[i].isupper() == True and i != 0 and i != (len(s) - 1):
                    hasUpper = True
                    break
            if hasUpper == True:
                hasDigit = False
                for i in range(0,len(s)):
                    if s[i].isdigit() == True and i != 0 and i != (len(s) - 1):
                        hasDigit = True
                        break
                if hasDigit == True:
                    hasSpecial = False
                    for i in range(0,len(s)):
                        if s[i] == '@' or s[i] == '#' or s[i] == '%' or s[i] == '&' or s[i] == '?':
                            if i != 0 and i != (len(s) - 1):
                                hasSpecial = True
                    if hasSpecial == False:
                        isValid = False
                else:
                    isValid = False
            else:
                isValid = False
        else:
            isValid = False
    else:
        isValid = False
    if isValid == True:
        print('YES')
    else:
        print('NO')