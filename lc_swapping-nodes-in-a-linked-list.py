class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        aN = None
        bN = None
        nF = k
        nL = n - k + 1
        temp = head
        z = 0
        while temp:
            z += 1
            if z == nF:
                aN = temp
            if z == nL:
                bN = temp
            temp = temp.next
        aN.val, bN.val = bN.val, aN.val
        return head

