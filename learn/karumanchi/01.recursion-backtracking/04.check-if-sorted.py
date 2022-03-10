def isArraySorted(arr):
    if len(arr) == 1:
        return True
    
    return arr[0] <= arr[1] and isArraySorted(arr[1:])

print(isArraySorted([1,2,3,3,4,5,6]))
print(isArraySorted([2,3,4,3,5])) 