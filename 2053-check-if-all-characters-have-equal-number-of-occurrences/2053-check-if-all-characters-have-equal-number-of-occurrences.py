from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        check = set()

        for char in s:
            counts[char] += 1
        # print(counts)
        for key in counts:
            print(counts[key])
            check.add(counts[key])
        if len(check) == 1:
            return True
        else:
            return False
       
       