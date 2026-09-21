"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pairs = {}
        curr = head
        while curr:
            pairs[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr_two = head
        while curr_two:
            if curr_two.next:
                pairs[curr_two].next = pairs[curr_two.next]
            if curr_two.random:
                pairs[curr_two].random = pairs[curr_two.random]
            curr_two = curr_two.next

        if not head:
            return None

        return pairs[head]





        