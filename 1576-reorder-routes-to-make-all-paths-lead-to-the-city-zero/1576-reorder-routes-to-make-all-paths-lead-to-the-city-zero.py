from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # graph => hashmap
        graph = defaultdict(list)
        road = set()
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            road.add((x, y))

        print(graph)
        print(road)

        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if(node, neighbor) in road:
                        ans += 1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans

        seen = {0}
        return dfs(0)