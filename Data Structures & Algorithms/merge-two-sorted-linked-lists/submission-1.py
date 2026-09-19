# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currA = list1
        currB = list2
        res = currC = ListNode(0, None)

        while currA and currB:
            if currA.val < currB.val:
                currC.next = currA
                currA = currA.next
            else:
                currC.next = currB
                currB = currB.next
            currC = currC.next

        if currA:
            currC.next = currA
        elif currB:
            currC.next = currB
            
        return res.next

        