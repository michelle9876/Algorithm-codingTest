# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 전역 리스트로 선언
        values = []
        def inorder(node):
            if not node:
                return 
            # 왼쪽 서브트리 탐색
            inorder(node.left)
            # 현재 노드 값 추가
            values.append(node.val)
            # 오른쪽 서브트리 탐색
            inorder(node.right)
        
        # 중위 순회 실행
        inorder(root)
        print(values)

        ans = float('inf')
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i-1])
        return ans

