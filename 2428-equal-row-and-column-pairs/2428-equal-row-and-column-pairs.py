from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_key(arr):
            return tuple(arr)  # 리스트를 튜플로 변환 (딕셔너리의 키로 사용하기 위해)
        
        row_dic = defaultdict(int)
        for row in grid:
            row_dic[convert_to_key(row)] += 1
        print(row_dic)

        # 3, 1, 2 = [0, 0], [0, 1], [0, 2]
        # 2, 7, 7 = [1, 0], [1, 1], [1, 2]
        
        col_dic = defaultdict(int)
        
        for col in range(len(grid[0])):  # 열의 개수만큼 반복
            curr_col = []
            for row in range(len(grid)):
                print(col, row, grid[row][col])
                curr_col.append(grid[row][col])
                # print(curr_col)
            col_dic[convert_to_key(curr_col)] += 1
        print(col_dic)

        ans = 0
        # for r_key in row_dic:
        #     for c_key in col_dic:
        #         if r_key == c_key:
        #             ans += row_dic[r_key] * col_dic[c_key]
        # return(ans)

        for key in row_dic:
            if key in col_dic:
                ans += row_dic[key] * col_dic[key]
        return ans




        