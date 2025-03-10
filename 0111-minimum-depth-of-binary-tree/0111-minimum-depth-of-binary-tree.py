# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # 한쪽 자식이 없으면, 존재하는 서브트리의 깊이를 사용
        if not root.left or not root.right:
            return left + right + 1
            
         # 둘 다 있으면 최소 깊이 선택
        return min(left, right) + 1

