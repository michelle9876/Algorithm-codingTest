class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # distinct -> set()
        arr1 = []
        arr2 = []
        
        num1 = set(nums1)
        num2 = set(nums2)
        
        for n1 in num1:
            if n1 not in num2:
                arr1.append(n1)
        for n2 in num2:
            if n2 not in num1:
                arr2.append(n2)
        return([arr1, arr2])