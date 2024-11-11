class Solution:
    def repeatedCharacter(self, s: str) -> str:
        info = set()
        # info = {"a": idx}
        for char in s:
            if char in info:
                return char
            info.add(char)
        print(info)