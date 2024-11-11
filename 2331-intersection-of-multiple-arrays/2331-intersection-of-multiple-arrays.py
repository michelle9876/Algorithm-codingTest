from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        counts = defaultdict(int)
        for arr in nums:
            for x in arr :
                if x in arr:
                    counts[x] += 1
        # print(counts)
        n = len(nums)
        answer = []
        for key in counts:
            if counts[key] == n : 
                answer.append(key)
        return sorted(answer)
                


        