class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {key: number, value: num position}
        dic = {}
        for i in range(len(nums)):
            value = i
            key = nums[i]
        # print(dic)
        # num1 + key = target
            num1 = target - key
            if num1 in dic:
                return [dic[num1], value]
                
            # add key,value in dic(cash) later
            dic[key] = value
        return [ ]



        










        # info = {}
        # # info = {"2": 0}
        # for idx in range(len(nums)):
        #     key = nums[idx]
        #     # num1 + num2 = target
        #     num1 = target - key
        #     if num1 in info:
        #         return([idx, info[num1]])
        #     if key not in info: 
        #         info[key] = idx
        #         # return [num1, key]
               
        

    

