class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # checking if s elements are in t
        # for se in s:
        #     if se not in t:
        #         return False
        # return True

        # 순서도 고려해야함!
        
        s_idx = 0
        t_idx = 0

        while len(s) > s_idx and len(t) > t_idx :
            if s[s_idx] == t[t_idx]:
                s_idx += 1  # s의 문자와 t의 문자가 같으면 s 인덱스 증가
            t_idx += 1 # 항상 t 인덱스 증가

    # return 키워드 뒤에 있는 표현식의 결과가 함수의 반환값으로 사용됩니다.
    # 따라서 s_idx == len(s)가 True일 경우 함수는 True를 반환하고, False일 경우 함수는 False를 반환합니다.
        return len(s) == s_idx
                    
        