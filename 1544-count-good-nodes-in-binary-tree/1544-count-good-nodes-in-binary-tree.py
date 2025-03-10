# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far ):
            if not node :
                return 0
            # 현재 노드가 "good node"인지 판단
            good = 1 if node.val >= max_so_far else 0
            left = dfs(node.left, max(max_so_far, node.val))
            right = dfs(node.right, max(max_so_far, node.val))

            return left + right + good
            
        # DFS 시작 (초기 최댓값은 -무한대)
        return dfs(root, float("-inf"))

        