'''
Question: https://practice.geeksforgeeks.org/problems/k-largest-elements3736/1/?company[]=Microsoft&company[]=Microsoft&difficulty[]=-1&page=1&query=company[]Microsoftdifficulty[]-1page1company[]Microsoft
'''
def kLargest(li,n,k):
    # code here
    li.sort()
    ans = []
    till = 0
    while till != k:
        ans.append(li.pop())
        till += 1
    return ans