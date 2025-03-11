# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        level_lists = []
        # 가장 깊은 레벨의 노드 값 합
        sum_val = 0
        while queue:
            current_level = len(queue)
            # 새로운 레벨 시작할 때 합 초기화
            sum_val = 0
            # print("level", current_level)
            for _ in range(current_level):
                node = queue.popleft()
                # 현재 레벨의 값 추가
                sum_val += node.val
                # print("node, sum:", node.val, sum_val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return sum_val # 가장 마지막 레벨의 합 반환

        