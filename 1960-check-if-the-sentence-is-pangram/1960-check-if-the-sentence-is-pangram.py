class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        seen = set()
        
        for alp in sentence:
            if alp in alphabet:
                seen.add(alp)
        if len(alphabet) == len(seen):
            return True
        else:
            return False
                