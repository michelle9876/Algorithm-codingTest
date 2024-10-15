class Solution:
    def singleNumber(self, nums: List[int]) -> int:

#  딕셔너리 사용해서 풀었을때!!
        # info = { }
        # # info = {"key-nums": "count"}

        # for i in nums:
        #     if i in info:
        #         info[i] += 1
        #     else:
        #         info[i] = 1

        # for num in info:
        #     if info[num] == 1:
        #         return num
# ======================================

#  XOR (^): 사용해보기!!!
# 두 비트가 서로 다르면 1, 같으면 0.
# 중복을 제거하거나 특정 값을 남기는 문제를 해결할 수 있습니다.
# 예: 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0

# XOR은 특히 유용한데, 같은 값을 두 번 XOR하면 원래 값으로 돌아오고, 한 번 XOR하면 그 값을 제거하는 효과가 있습니다.
        result = 0
        for i in nums:
            if i in nums:
                result ^= i
        return result