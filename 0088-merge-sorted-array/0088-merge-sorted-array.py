# nums1.length == m + n
# nums2.length == n
# m = num1.length - n(num2.length)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
          # m과 n은 nums1과 nums2의 중요한 숫자 개수를 나타내요.
        i = m - 1  # nums1의 중요한 숫자들 중에서 마지막 숫자의 위치
        j = n - 1  # nums2의 마지막 숫자의 위치
        k = m + n - 1  # 합쳐질 리스트에서 마지막 위치

        # nums2의 숫자들을 모두 처리할 때까지 반복해요.
        while j >= 0:
            # nums1의 남은 숫자와 nums2의 숫자를 비교해요.
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # nums1의 숫자가 더 크면 nums1의 숫자를 뒤에서 앞으로 이동
                i -= 1  # nums1의 숫자를 하나 줄여요
            else:
                nums1[k] = nums2[j]  # nums2의 숫자가 더 크면 nums2의 숫자를 뒤에서 앞으로 이동
                j -= 1  # nums2의 숫자를 하나 줄여요
            k -= 1  # 합쳐진 리스트의 위치를 하나 줄여요
        