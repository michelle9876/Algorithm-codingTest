class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        ans = 0

        def vaild(row, col):
            return (0 <= row < m) and (0 <= col < n) and grid[row][col] == "1"

        def dfs(row, col):
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if vaild(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in seen:
                    ans += 1 
                    seen.add((row, col))
                    dfs(row, col)
        return ans