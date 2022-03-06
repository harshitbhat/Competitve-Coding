def oddOccuring(arr):
    ans = 0

    for num in arr:
        ans ^= num
    
    return ans

array = [4, 3, 3, 4, 4, 4, 5, 3, 5];
print(f'Odd occurring element is {oddOccuring(array)}');