'''
Question:  https://practice.geeksforgeeks.org/problems/square-root/1/?company[]=Microsoft&company[]=Microsoft&difficulty[]=-1&page=1&query=company[]Microsoftdifficulty[]-1page1company[]Microsoft#
'''
def floorSqrt(x): 
    #Your code here
    if x == 0 or x == 1:
        return x
    start = 1
    end = x
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans