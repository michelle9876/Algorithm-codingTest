class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        n = len(nums)
        # remove_arr = [ ]

        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
      