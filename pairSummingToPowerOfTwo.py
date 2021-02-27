def pairSummingToPowerOfTwo(arr):
    powerOfTwos = []
    k = 0
    for i in range(30):
        powerOfTwos.append(2**k)
        k += 1
    numbers = {}
    for i in range(0,len(arr)):
        numbers[arr[i]] = i 
    
    ans = 0
    for i in range(0,len(arr)):
        for totalSum in powerOfTwos:
            if (totalSum - arr[i]) in numbers.keys():
                if numbers[totalSum - arr[i]] <= numbers[arr[i]]:
                    ans += 1
    return ans

print(pairSummingToPowerOfTwo([1,-1,2,3]))