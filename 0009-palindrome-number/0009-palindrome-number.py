class Solution:
    def isPalindrome(self, x: int) -> bool:
        stackNum = []
        
        for num in str(x):
            stackNum.append(num)
        # print(stackNum)

        for num in str(x):
            if num != stackNum.pop():
                return False       
        return True
        