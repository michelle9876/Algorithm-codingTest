class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        checked = set()
        result = []

        for n in nums:
            if n not in checked:
                result.append(n)
                checked.add(n)
                
    # result의 값을 nums의 앞부분에 덮어쓰는 코드
        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)

        
    
        
