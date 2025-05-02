class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        seen = set()
        count = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def vaild(row, col):
            return 0 <= row < r and 0 <= col < c and grid[row][col] == '1'

        def dfs(row, col):
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if vaild(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)
            
        for row in range(r):
            for col in range(c):
                if grid[row][col] == '1' and (row, col) not in seen:
                    count += 1
                    seen.add((row, col))
                    dfs(row, col)
        return count

















        # m = len(grid)
        # n = len(grid[0])
        # seen = set()
        # count = 0
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # def valid(row, col):
        #     return 0 <= row < m and 0 <= col < n and grid[row][col] == '1'

        # def dfs(row, col):
        #     for nr, nx in directions:
        #         next_row, next_col = row + nr, col + nx
        #         if valid(next_row, next_col) and (next_row, next_col) not in seen:
        #             seen.add((next_row, next_col))
        #             dfs(next_row, next_col)



        # for row in range(m):
        #     for col in range(n):
        #         if grid[row][col] == '1' and (row, col) not in seen:
        #             count += 1
        #             seen.add((row, col))
        #             dfs(row, col)

        # return count

       