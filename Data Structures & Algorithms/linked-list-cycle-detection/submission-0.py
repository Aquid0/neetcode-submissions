# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head

        while curr:
            if str(curr.val)[-1] == "!":
                return True
            curr.val = str(curr.val) + "!"
            curr = curr.next
        
        return False