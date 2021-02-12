'''
Question Link: https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1/?company[]=Microsoft&company[]=Microsoft&difficulty[]=-1&page=1&query=company[]Microsoftdifficulty[]-1page1company[]Microsoft
'''

def minValue(root):
    if root.left == None:
        return root.data
    return minValue(root.left)