# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0   # 트리의 최대 지름을 저장할 변수

        def dfs(node):
            # 노드가 없으면 깊이 0
            if not node:
                return 0
            
            # path = max(len(node)) - 1 
            left = dfs(node.left)  # 왼쪽 서브트리의 깊이
            right = dfs(node.right) # 오른쪽 서브트리의 깊이

             # 현재 노드를 포함한 지름 계산 (왼쪽 깊이 + 오른쪽 깊이)    
            self.diameter = max(self.diameter, left + right)

             # 노드의 깊이를 반환 (자식 노드 중 더 깊은 쪽 + 1)
            return max (left, right) + 1
        
        dfs(root)  # DFS 실행
        return self.diameter # 최종 지름 반환

        