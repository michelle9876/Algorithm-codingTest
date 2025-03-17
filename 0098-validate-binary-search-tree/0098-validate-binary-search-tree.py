# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            # BST의 조건 위반
            if not node:
                return True

            # BST의 조건 위반
            if not (small < node.val < large):
                return False

            # 왼쪽 서브트리는 `small < 값 < node.val` 범위여야 함
            # 오른쪽 서브트리는 `node.val < 값 < large` 범위여야 함
            left = dfs(node.left, small, node.val)
            right = dfs(node.right, node.val, large)
            return left and right
            
        return dfs(root, float('-inf'), float('inf'))
            
        