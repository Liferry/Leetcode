# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        Args:
            head: ListNode
        
        Return:
            ListNode
        """
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
        

# class Solution:
#     def reverseList(self, head):
#         """
#         Args:
#             head: ListNode
        
#         Return:
#             ListNode
#         """
#         if not head or not head.next:
#             return head
#         new_head = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return new_head