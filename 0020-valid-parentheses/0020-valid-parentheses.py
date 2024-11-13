class Solution:
    def isValid(self, s: str) -> bool:
        # must be closed by same type of brackets
        # must be closed in the correct order
        # corresponding open bracket of same type
        stack = []
        dic_match = {"(": ")", "{" : "}", "[": "]"} 
        
        for symbol in s :
            if symbol in dic_match:
                stack.append(symbol)
            else:
                if not stack:
                    return False

                previous_opening = stack.pop()
                if dic_match[previous_opening] != symbol:
                    return False
        return not stack

       