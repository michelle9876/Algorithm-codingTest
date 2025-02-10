from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        n = len(nums)

        for sublist in nums:
            for num in set(sublist): # 각 리스트 내 중복 제거
                count[num] += 1
        
        # 모든 리스트에서 등장한 숫자만 필터링하여 정렬된 리스트로 반환
        return sorted([key for key, value in count.items() if value == n])
        
        # count = defaultdict(int)
        # n = len(nums)
        # dic = {}
        # for i in range(n) :
        #     for j in range(len(nums[i])):
        #         if nums[i][j] not in dic:
        #             count[nums[i][j]] += 1
    
        # key_result = [key for key, value in count.items() if value == n]
        # return sorted(key_result)