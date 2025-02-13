from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            # groups[key] = word
            groups[key].append(word)
        # print(groups)
        return list(groups.values())