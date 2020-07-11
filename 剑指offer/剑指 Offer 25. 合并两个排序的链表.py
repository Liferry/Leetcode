# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        Args:
            l1: ListNode
            l2: ListNode
        
        Return:
            ListNode
        """
        dummy = ListNode(None)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        
        if l2:
            l1 = l2
        
        while l1:
            cur.next = ListNode(l1.val)
            l1 = l1.next
            cur = cur.next
        
        return dummy.next
        