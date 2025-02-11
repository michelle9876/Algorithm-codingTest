from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        curr = ans = 0
        counts[0] = 1   # 초기 상태 저장
        for num in nums:
            if num % 2 == 1:
                curr += 1
            ans += counts[curr - k]   # k개 전 상태가 몇 번 등장했는지 확인
            counts[curr] +=  1  # 현재 상태 저장
        print(curr)
        print(ans)
        return ans
        