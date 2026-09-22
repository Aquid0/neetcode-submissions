# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = l1 if l1 else ListNode(0, None)

        currL1 = l1 
        currL2 = l2
        carry = 0

        # summing into list 1
        while True:
            vl1 = currL1.val if currL1 else 0
            vl2 = currL2.val if currL2 else 0
            s = vl1 + vl2 + carry

            if s >= 10:
                carry = 1
                s -= 10
            else: 
                carry = 0
            
            currL1.val = s

            if (not currL1.next and ((currL2 and currL2.next) or carry)):
                currL1.next = ListNode(0, None)

            currL1 = currL1.next

            if currL2: 
                currL2 = currL2.next
        
            if not currL1 and not currL2:
                break
        
        return l1
                
                

