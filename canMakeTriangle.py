def check(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False
def solve(arr):
    ans = []
    for i in range(0,len(arr)-1):
        if check(arr[i],arr[i+1],arr[i+2]):
            ans.append(1)
        else:
            ans.append(0)
