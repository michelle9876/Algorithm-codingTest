# flowerbed : 0 --> empty, 1 --> not empty
# n : new flowers can be planted --> true/ otherwise: false

# 조건 확인: 꽃을 심을 수 있는 조건은 현재 위치가 0이고, 그 앞과 뒤의 위치도 0일 때입니다. 배열의 경계를 넘지 않도록 주의해야 합니다.
# 배열 수정: 꽃을 심으면 해당 위치를 1로 바꿉니다. 이로 인해 같은 위치에 다시 꽃을 심지 않도록 합니다.
# 계산 종료: 만약 새로운 꽃을 모두 심었다면 더 이상 탐색할 필요 없이 True를 반환합니다. 끝까지 탐색했는데도 꽃을 다 심지 못했다면 False를 반환합니다.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        lengthF = len(flowerbed)

        if n == 0:
            return True

        for i in range(lengthF):
            if flowerbed[i] == 0:
                pre = (i == 0 or flowerbed[i - 1] == 0 )
                post = (i == lengthF - 1  or flowerbed[i + 1] == 0)
                if pre and post:
                    count += 1
                    flowerbed[i] = 1
            
                    if count >= n:
                        return True
        return False

           