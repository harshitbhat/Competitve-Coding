'''
    Question Link: https://practice.geeksforgeeks.org/problems/binary-representation5003/1/?company[]=Microsoft&company[]=Microsoft&difficulty[]=-2&page=1&query=company[]Microsoftdifficulty[]-2page1company[]Microsoft

    
'''

def getBinaryRep(n):
    temp = ''
    while n:
        temp += str(n%2)
        n = n//2
    return '0' * (30-len(temp)) + temp[::-1]

print(getBinaryRep(12))