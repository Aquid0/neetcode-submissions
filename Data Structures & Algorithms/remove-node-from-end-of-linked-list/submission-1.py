# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        j = 0
        endNode = head
        while endNode:
            endNode = endNode.next
            j += 1

        target = j - n
        curr = head

        if target == 0:
            return curr.next

        for i in range(j - 1):
            if (i + 1) == target:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
        