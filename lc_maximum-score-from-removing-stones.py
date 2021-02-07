import math
def maximumScore(a,b,c):
    arr = [a,b,c]
    arr.sort()
    if (arr[0] + arr[1]) <= arr[2]:
        return arr[0] + arr[1]
    else:
        steps = math.ceil(((arr[0] + arr[1]) - arr[2]) / 2)
        arr[0] -= steps
        arr[1] -= steps
        if steps == 0:
            return min(arr[1],arr[2])
        return steps + arr[0] + arr[1]


print(maximumScore(4,5,6))
