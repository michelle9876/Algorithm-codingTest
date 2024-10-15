class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        

        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    # left는 target이 들어갈 수 있는 위치를 항상 가리킵니다. 
    # while문이 끝날 때 left는 배열에서 target보다 크거나 같은 값이 처음으로 등장하는 위치를 가리킵니다.
        return left


        


            
        


        