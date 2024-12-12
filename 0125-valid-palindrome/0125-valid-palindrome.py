from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # uppercase --> lowercase : lower()
        # remove all non-alphanumeric chars : .isalnum()
        # read same forward and backward
        # for ch in s:
        dq = deque()

        lowerCase = s.lower()
        for letter in lowerCase:
            if letter.isalnum() == True:
                dq.append(letter)
        
        while len(dq) > 1:
            first = dq.popleft()
            last = dq.pop()
            
            if first != last:
                return False
        return True
