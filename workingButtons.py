def workingButtons(digits,words):
    hash = {
        0 : [],
        1: [],
        2 : ['a','b','c'],
        3 : ['d','e','f'],
        4 : ['g','h','i'],
        5 : ['j','k','l'],
        6 : ['m','n','o'],
        7 : ['p','q','r','s'],
        8 : ['t','u','v'],
        9 : ['w','x','y','z']
    }
    check = []
    for dig in digits:
        a = hash[dig]
        for i in a:
            check.append(i)
    ans = []
    for word in words:
        isPossible = True
        for i in word:
            if i not in check:
                isPossible = False
                break
        ans.append(isPossible)
    return ans

a = workingButtons([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],['abc','gdef','x'])
print(a)