class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # r_hashmap = {}
        # m_hashmap = {}

        # for r in ransomNote:
        #     if r in r_hashmap:
        #         r_hashmap[r] += 1
        #     else:
        #         r_hashmap[r] = 1

        # for m in magazine:
        #     if m in m_hashmap:
        #         m_hashmap[m] += 1
        #     else:
        #         m_hashmap[m] = 1

        # for r_key in r_hashmap:
        #     if r_key not in m_hashmap:
        #         return False
        #     if r_hashmap[r_key] > m_hashmap[r_key]:
        #         return False
        
        # return True
    

    # magazine의 문자 빈도를 저장
        char_count = {}

        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # ransomNote를 순회하며 요구 문자 확인
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        return True


        