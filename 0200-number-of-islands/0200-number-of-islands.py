class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return
            else:
                    grid[i][j] = '0'
                    dfs(i, j+1)
                    dfs(i+1, j)
                    dfs(i, j-1)
                    dfs(i-1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  
                    count += 1
                    dfs(i, j)

        return count
