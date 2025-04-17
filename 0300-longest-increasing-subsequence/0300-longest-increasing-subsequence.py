class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dp(i):
            # base case
            # 기본값: 자기 자신 하나만 포함하는 경우
            ans = 1
             # 이미 계산한 값이 있다면 반환
            if i in memo:
                return memo[i]

            # Recurrence relation
            # 0부터 i-1까지의 j에 대해 nums[j] < nums[i] 이면 수열 가능
            for j in range(i):
                if nums[j] < nums[i]:
                    ans = max(ans, dp(j)+ 1)
            # 계산된 값을 캐시에 저장
            memo[i] = ans
            return ans

        memo = {}

        return max(dp(i) for i in range(len(nums)))
        