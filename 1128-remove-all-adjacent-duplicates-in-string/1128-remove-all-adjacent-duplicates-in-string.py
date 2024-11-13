class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack  = []
        for alph in s:
            if stack and stack[-1] == alph:
                stack.pop()
            else:
                stack.append(alph)
        return "".join(stack)        