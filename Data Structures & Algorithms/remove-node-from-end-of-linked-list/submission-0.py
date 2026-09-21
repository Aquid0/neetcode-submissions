# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        j = 1
        endIndex = 0
        endNode = head
        while endNode.next:
            endNode = endNode.next
            j += 1

        if j == 1: 
            return None

        target = j - n
        i = 0
        curr = head

        if target == 0:
            return curr.next

        while i < target - 1:
            i += 1 
            curr = curr.next

        if not curr.next.next:
            curr.next = None
            return head
        else:
            curr.next = curr.next.next
            return head
        