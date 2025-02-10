from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        set_s = set(s)

        for char in s:
            count[char] += 1
        
        # print(count)

        if len(set(count.values())) == 1 :
            return True
        else: 
            return False
        