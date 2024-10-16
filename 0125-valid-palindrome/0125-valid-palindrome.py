from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # uppercase --> lowercase
        # remove all non-alphanumeric chars
        # read same forward and backward
        # for ch in s:
        
        dq = deque()

        lowerCase = s.lower()
        for lo in lowerCase:
            if lo.isalnum() == True:
                dq.append(lo)
    

        while len(dq) > 1 :
            start = dq.popleft()
            end = dq.pop()
            if start != end:
                return False
                 
        return True