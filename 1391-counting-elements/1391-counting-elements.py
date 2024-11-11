class Solution:
    def countElements(self, arr: List[int]) -> int:
        # Input: arr = [1,2,3]
        # Output: 2
        # Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
        
        hashSet = set(arr)
        count = 0
        for num in arr:
            checkNum = num + 1
            if checkNum in hashSet:
                count += 1
        
        return count