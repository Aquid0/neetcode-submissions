# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(list1, list2):
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

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(mergeTwoLists(l1, l2))
            lists = merged

        return lists[0]