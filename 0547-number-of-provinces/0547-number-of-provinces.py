from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        visited = set()

        def dfs(city):
            visited.add(city)
            for neighbor in range(n):
                if neighbor not in visited and isConnected[city][neighbor] == 1:
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                dfs(city)
                count += 1
        return count
