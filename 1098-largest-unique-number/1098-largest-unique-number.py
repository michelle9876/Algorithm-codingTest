from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
            # print(counts)
         
        # once_nums = [key if value == 1 else -1 for key, value in counts.items()]
        once_nums = [key for key, value in counts.items() if value == 1]
        return max(once_nums) if once_nums else -1