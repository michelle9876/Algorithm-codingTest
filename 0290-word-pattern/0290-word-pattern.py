class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternDict = {}
        sDict = {}
        
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        for char, word in zip(pattern, words):
            if ((char in patternDict and patternDict[char] != word) or (word in sDict and sDict[word] != char)):
                return False
            patternDict[char] = word
            sDict[word] = char
        print(patternDict)
        print(sDict)
        return True
        

 
        

            

        