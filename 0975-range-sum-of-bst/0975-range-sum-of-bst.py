# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        ans = 0
        # 현재 노드 값이 범위 안에 있는지 확인
        if low <= root.val <= high:
            ans += root.val
        #  왼쪽 서브트리 탐색 (작은 값들)
        if low < root.val:
            ans += self.rangeSumBST(root.left, low, high)
        #  오른쪽 서브트리 탐색 (큰 값들)
        if root.val < high:
            ans += self.rangeSumBST(root.right,low, high)

        return ans

        