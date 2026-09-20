# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """

        0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        L                             R

        
        temp = node @ L + 1 ( 1 -> 2 -> ... )
        curr.next = R ( 0 -> 6 -> None )
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        second = slow.next 
        prev = None
        slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        
        f = head # head of first list
        s = prev # head of reversed list
        while s:
            t1 = f.next
            t2 = s.next
            f.next = s
            s.next = t1
            f = t1
            s = t2
        
