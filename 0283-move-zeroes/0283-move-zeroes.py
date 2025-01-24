class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Input: nums = [0,1,0,3,12]
        # Output: [1,3,12,0,0]
        
        # 0이 아닌 값을 저장할 위치
        non_zero_index = 0
        n = len(nums)
        
        # 1. 0이 아닌 요소를 앞쪽으로 이동
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
                
        # 2. 나머지 위치를 0으로 채움
        for i in range(non_zero_index, n):
            nums[i] = 0
        
#         for i in range(n-1, -1, -1):
#             # print(i)
#             while i != currPoint :
#                 if nums[currPoint] == 0 :
#                     nums[-1] = nums[currPoint]
#                     currPoint += 1
#                 if nums[i] == 0:
#                     nums[-1] = nums[i]
                
#                 if i== currPoint:
#                     break
#         print(nums)
            
                    
                    
                    
                
 
                
                

        