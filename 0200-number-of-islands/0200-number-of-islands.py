class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == '1'

        def dfs(row, col):
            for nr, nx in directions:
                next_row, next_col = row + nr, col + nx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)



        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1' and (row, col) not in seen:
                    count += 1
                    seen.add((row, col))
                    dfs(row, col)

        return count

        # m = len(grid)
        # n = len(grid[0])
        # count = 0

        # def dfs(i, j):
        #     if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
        #         return
        #     else:
        #             grid[i][j] = '0'
        #             dfs(i, j+1)
        #             dfs(i+1, j)
        #             dfs(i, j-1)
        #             dfs(i-1, j)

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':  
        #             count += 1
        #             dfs(i, j)

        # return count
