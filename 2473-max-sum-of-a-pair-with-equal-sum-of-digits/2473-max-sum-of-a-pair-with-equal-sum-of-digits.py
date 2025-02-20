from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Conditions1: a sum of digits equal to
        # return max sum
        # if no two numbers that satisfy , return -1
        
        def get_digits_sum(num):
            # for num in nums:
            digit_sum = 0
            while num:
                digit_sum += num % 10  # 마지막 자리 숫자를 더함
                num //= 10              # 마지막 자리 숫자 제거
            return digit_sum
        
        dic = defaultdict(list)
        for num in nums:
            digit_sum = get_digits_sum(num)
            dic[digit_sum].append(num)
        print(dic)
        
        max_sum = -1
        for value in dic.values():
            # print(value)
            if len(value) > 1:
                value.sort(reverse=True) # 내림차순 정렬
                print(value)
                max_sum = max(max_sum, value[0]+ value[1]) # 가장 큰 두 개의 숫자 합 갱신
        return max_sum

        # for key, value in dic.items():
        #     sum_num = 0
        #     if len(value) != 1: 
        #         for v in value:
        #             sum_num += v
        #     # print(sum_num)
        #         return max(sum_num, v)
        # return -1



          