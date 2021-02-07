def check(nums):
    if len(nums) <= 2:
        return True
    changeN = 0
    for i in range(0,len(nums)-1):
        if nums[i] > nums[i+1]:
            changeN += 1
    if nums[len(nums)-1] > nums[0]:
        changeN += 1
    if changeN <= 1:
        return True
    else:
        return False

print(check([2,1]))