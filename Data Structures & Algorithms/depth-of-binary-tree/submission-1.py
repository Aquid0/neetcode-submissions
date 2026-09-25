# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import copy

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        t = deque([])
        res = 0
        curr = None

        while True:
            while q: 
                curr = q.popleft()
                if curr.left: 
                    t.append(curr.left)
                if curr.right: 
                    t.append(curr.right)
                
            res += 1

            if not t: 
                break
            else: 
                q = copy.deepcopy(t)
                t = deque([])

        return res
        