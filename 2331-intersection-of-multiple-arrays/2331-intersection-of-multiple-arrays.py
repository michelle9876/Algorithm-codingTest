from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        n = len(nums)
        dic = {}
        for i in range(n) :
            for j in range(len(nums[i])):
                if nums[i][j] not in dic:
                    count[nums[i][j]] += 1
        # print(count)
        
        # for key, value in count.items():
        #     if value == n :
        #         return [key]
        key_result = [key for key, value in count.items() if value == n]
        return sorted(key_result)