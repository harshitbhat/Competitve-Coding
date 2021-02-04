n,k = map(int,input().split())

arr = [0] * n
sumArray = [0] * n

def findArray(arr,sumArray,n,k,index,sum):
    if index >= k and sum < 0:
        return
    if sum > 0:
        arr[index - 1] = index
        sum = sum + arr[index - 1]
        sumArray[index - 1] = sum
        return findArray(arr,sumArray,n,k,index+1,sumArray[index-1])
    else:
        arr[index-1] = index * -1
        sum = sum + arr[index - 1]
        sumArray[index - 1] = sum
        return findArray(arr,sumArray,n,k,index+1,sumArray[index-1])
    


arr[0] = 1
sumArray[0] = 1

findArray(arr,sumArray,n,k,2,sumArray[0])
print(arr)
print(sumArray)