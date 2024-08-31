class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colour = [0 for _ in range(n)]

        def dfs(i, col):
            if colour[i] == col:
                return True
            if colour[i] != 0:
                return False
            colour[i] = col
            for neighbour in graph[i]:
                if not dfs(neighbour, -1 * col):
                    return False
            return True 

        for i in range(n):
            if colour[i] == 0 and not dfs(i, 1):
                return False

        return True
