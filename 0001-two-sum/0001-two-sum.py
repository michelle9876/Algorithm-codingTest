class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        info = {}
        # info = {"2": 0}
        for idx in range(len(nums)):
            key = nums[idx]
            # num1 + num2 = target
            num1 = target - key
            if num1 in info:
                return([idx, info[num1]])
            if key not in info: 
                info[key] = idx
                # return [num1, key]
               
        

    


        # output = []
        
        # for i in range(len(nums)):
        #     i_val = nums[i]
        #     for j in range(1, len(nums)):
        #         j_val = nums[j]
        #         if i == j:
        #             break
        #         if i_val + j_val == target :
        #             output.append(i)
        #             output.append(j)
        #             return output