class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return  indices of the two numbers!
        # dic = {2: 0, 7: 1, 11: 2, 15: 3} --> key: num, values: idx
        # num1 + num2 = target ==> num1 = target - num2 

        dic = {}
        for i in range(len(nums)):
            key = nums[i]
            value = i

            complement = target - key
        
            if complement in dic: # 이미 저장된 값인지 확인
                return [i, dic[complement]]

            dic[key] = i   # 현재 값과 인덱스를 저장
        


        