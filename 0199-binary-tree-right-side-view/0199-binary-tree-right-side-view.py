# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [ ]
        ans = []    
        queue = deque([root])
        while queue:
            nodes_current_level = len(queue)
            # this is the rightmost node(the last element of the queue) for the current level
            ans.append(queue[-1].val)
            for _ in range(nodes_current_level):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
        