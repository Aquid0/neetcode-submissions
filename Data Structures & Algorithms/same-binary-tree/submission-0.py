# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_p = deque([p])
        q_q = deque([q])

        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
            
        while q_p and q_q:
            p = q_p.popleft()
            q = q_q.popleft()

            if p.val != q.val: 
                return False

            # check if their child nodes are the same order
            if p.left and q.left: 
                q_p.append(p.left)
                q_q.append(q.left)
            elif p.left or q.left:
                return False
            
            if p.right and q.right:
                q_p.append(p.right)
                q_q.append(q.right)
            elif p.right or q.right:
                return False

        return True