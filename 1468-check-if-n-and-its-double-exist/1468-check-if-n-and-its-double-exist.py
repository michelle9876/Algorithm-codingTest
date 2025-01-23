class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
    # i != j
    # 0 <= i, j < arr.length
    # arr[i] == 2 * arr[j]
    
    # Input: arr = [10,2,5,3]
    # Output: true
    # Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
    
    # Input: arr = [3,1,7,11]
    # Output: false
    # Explanation: There is no i and j that satisfy the conditions.
        
        # 이미 확인한 숫자들을 저장할 집합
        seen = set()
        
        for num in arr:
             # 현재 숫자의 두 배 또는 절반이 이미 존재하는지 확인
            if 2 * num in seen or ( num % 2 == 0 and num // 2 in seen):
                return True
            # 현재 숫자를 집합에 추가
            seen.add(num)
        return False

    
#         k = 0
#         n = len(arr)
#         # adge case
#         if n <= 1:
#             return False

#         for i in range(1, n):
#             if i != k:
#                 if arr[i] == 2 * arr[k]:
#                     k += 1
#                     return True

#         return False            
            
        
        
        
        
        
        