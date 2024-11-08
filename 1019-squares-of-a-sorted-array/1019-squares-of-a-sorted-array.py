class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Input: nums = [-4,-1,0,3,10]
        # Output: [0,1,9,16,100]
        # Explanation: After squaring, the array becomes [16,1,0,9,100].
        # After sorting, it becomes [0,1,9,16,100].

        res = [0] * len(nums)
        left = 0
        right = len(nums) -1

        for i in range(len(nums)-1 , -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1

        return res
        # new = []
        # for i in nums:
        #     new.append(i*i)
             
        # # print(new)
       
        # for front_idx in range(0, len(new) -1 ):
        #     for idx in range(0, len(new) -1 - front_idx):
        #         if new[idx] > new[idx+1]:
        #             new[idx], new[idx+1] = new[idx+1], new[idx]
        # return new