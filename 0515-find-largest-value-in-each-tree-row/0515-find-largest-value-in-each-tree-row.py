# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from  collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [ ]
        
        queue = deque([root])
        # 각 레벨의 최대값을 저장할 리스트
        ans = []

        while queue:
            current_level = len(queue)
             # 각 레벨마다 최대값 초기화
            largest_val = float("-inf")

            for _ in range(current_level):
                node = queue.popleft()
                largest_val = max(largest_val, node.val) # 최대값 갱신

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(largest_val) # 해당 레벨의 최대값 저장
        return ans # 모든 레벨의 최대값 리스트 반환
                