def sumOfUnique(nums):
    dict = {}
    for i in nums:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    ans = 0
    for i in dict:
        if dict[i] == 1:
            ans += i
    return ans