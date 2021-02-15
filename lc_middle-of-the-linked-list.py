# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        n = n // 2 
        i = 0
        temp = head
        while i != n:
            i += 1
            temp = temp.next
        return temp