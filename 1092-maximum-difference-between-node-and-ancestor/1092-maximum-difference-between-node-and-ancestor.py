# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs (node, max_val, min_val):
         # 더 이상 탐색할 노드가 없으면 현재까지의 최댓값과 최솟값 차이를 반환.
            if not node:
                return max_val - min_val

            
            max_val = max(max_val, node.val)  # 최댓값 갱신
            min_val = min(min_val, node.val)  # 최솟값 갱신

            # 왼쪽 서브트리 탐색
            left = dfs(node.left, max_val, min_val)
            # 오른쪽 서브트리 탐색
            right = dfs(node.right, max_val, min_val)

            return max(left, right)
        
        return dfs(root, root.val, root.val)
        
        