# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        n = 0
        while temp:
            n += 1
            temp = temp.next
        ans = 0
        ind = n-1
        temp = head
        while temp != None:
            ans += temp.val * (2**ind)
            ind -= 1
            temp = temp.next
        return ans