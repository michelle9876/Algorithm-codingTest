class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_hashmap = {}
        m_hashmap = {}

        for r in ransomNote:
            if r in r_hashmap:
                r_hashmap[r] += 1
            else:
                r_hashmap[r] = 1

        for m in magazine:
            if m in m_hashmap:
                m_hashmap[m] += 1
            else:
                m_hashmap[m] = 1

        for r_key in r_hashmap:
            if r_key not in m_hashmap:
                return False
            if r_hashmap[r_key] > m_hashmap[r_key]:
                return False
        
        return True
                

        