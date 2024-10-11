class Solution:
    def removeStars(self, s: str) -> str:
        # s : contains stars *
        # remove the closest non-star(left) + start itself
        stack = []
        for letter in s :
            if letter == "*":
                stack.pop()
                pass
            else:
                stack.append(letter)
                
        ans = ''.join(stack)        
        return (ans)
            
        

