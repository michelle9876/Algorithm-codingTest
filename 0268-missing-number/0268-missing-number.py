class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         Input: nums = [0,1]
#         Output: 2
#         Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the           missing number 
        
        maxNum = len(nums)
        # seen = set()
        for num in range(maxNum + 1):
            if num not in nums:
                return num