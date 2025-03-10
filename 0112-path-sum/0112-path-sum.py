# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # node: 현재 탐색중인 노드 / curr: 현재까지의 경로 합
        def dfs(node, curr):
            # 기저 사례 (재귀 종료 조건)
            if not node:
                return False

            # 경로의 끝인지 확인
            # 현재 node가 리프 노드(즉, 왼쪽 자식과 오른쪽 자식이 없는 노드)인지 확인
            # 만약 리프 노드라면, 현재까지의 합 curr + node.val이 targetSum과 일치하는지 확인하고,
            # 일치하면 True, 그렇지 않으면 False를 반환
            if node.left == None and node.right == None:
                return (curr + node.val) == targetSum
            
            # 현재 노드의 값을 합산
            curr += node.val
            # 왼쪽과 오른쪽 서브트리 탐색
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            return left or right
        # 루트 노드 root에서 시작하여 dfs 탐색을 시작 ( 초기 curr값 : 0)
        return dfs(root, 0)

        