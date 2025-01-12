class Solution:
    def findNumbers(self, nums: List[int]) -> int:
#         1. Find the number of digits
#         2. check that number if it is even! (x % 2 == 0)
#           ex) [12,345,2,6,7896]
        count = 0
        for num in nums:
            len_num = len(str(num))
            
            if (len_num % 2 == 0):
                count += 1
        return count