from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
#      Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
#      Output: [[1,2,10],[4,5,7,8]]

        seen = set()   # 모든 등장한 선수 (승자 + 패자)
        counts = defaultdict(int)   # 패배 횟수를 저장할 딕셔너리
        
        for win, lose in matches:
            seen.add(win)   
            seen.add(lose)   
            # print(seen)
            counts[lose] += 1  # 패배 횟수 증가
            # print(counts)
            
        # 한 번도 패배하지 않은 선수: counts에 없는 선수
        never_lost = sorted([player for player in seen if player not in counts])
        
        # 정확히 한 번 패배한 선수
        lost_once = sorted([player for player, lost_count in counts.items() if lost_count == 1])
        
        return [never_lost, lost_once]
        
#         for match in matches:
#             # print(match)
#             for value in match:
#                 win = match[0]
#                 lose = match[1]
#                 if value != lose:
#                     seen.add(value)
#             # print(lose)
#             counts[lose] += 1
#         # print(counts)
                
#         print(seen)
#         lostOnce = [key for key, value in counts.items() if value == 1]
#         print(sorted(lostOnce))
            