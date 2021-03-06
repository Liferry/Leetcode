# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head, val):
        """
        :param head: ListNode
        :param val: int

        :return: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head

        cur = dummy
        while cur.next and cur.next.val != val:
            cur = cur.next
        
        if cur.next:
            cur.next = cur.next.next
        
        return dummy.next
