class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # {key : index}
        s_dic = {}
        t_dic = {}
        if len(s) != len(t):
            return False

        for idx in range(len(s)):
            s_key = s[idx]
            t_key = t[idx]
            if s_key not in s_dic:
                s_dic[s_key] = idx
            
            if t_key not in t_dic:
                t_dic[t_key] = idx

            if s_dic[s_key] != t_dic[t_key]:
                return False
        
        return True


        # for sd in range(len(s)):
        #     value = sd
        #     key = s[sd]
        #     if key not in s_dic:
        #         s_dic[key] = value

        # for td in range(len(t)):
        #     value = td
        #     key = t[td]
        #     if key not in t_dic:
        #         t_dic[key] = value

        # s_values = s_dic.values()
        # t_values = t_dic.values()

        # if sorted(s_values) == sorted(t_values):
        #     print(sorted(s_values))
        #     print(sorted(t_values))
        #     return True
        # else:
        #     return False

        
    
       

        