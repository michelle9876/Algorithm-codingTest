# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [ ]
        
        queue = deque([root])
        final_ans = []
        print("finalAns:" ,final_ans)
        left_to_right = True

        while queue:
            current_level = len(queue)
            print("level:", current_level)

            # `deque` 사용하여 앞뒤로 추가 가능
            ans = []
            for _ in range(current_level):
                node = queue.popleft()
                ans.append(node.val)
               
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # `[::-1]`로 역순 처리 : 짝수 레벨에서는 그대로, 홀수 레벨에서는 뒤집어서 저장
            final_ans.append(ans if left_to_right else ans[::-1])
            # 방향 변경
            left_to_right = not left_to_right

        return final_ans