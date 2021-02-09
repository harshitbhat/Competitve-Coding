def validMountainArray(arr):
    if len(arr) <= 2:
        return False
    peak = max(arr)
    pos = arr.index(peak)
    if pos == 0 or pos == len(arr) - 1:
        return False
    i = pos - 1
    while i >= 0:
        if arr[i] >= arr[i+1]:
            return False
        i -= 1
    j = pos + 1
    while j < len(arr):
        if arr[j] >= arr[j-1]:
            return False
        j += 1
    return True
print(validMountainArray([0,1,2,3,4,5,6,7,8,9]))