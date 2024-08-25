class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph) - 1

        def dfs(node, r):
            r.append(node)
            for i in graph[node]:
                dfs(i, r.copy())
            if node == n:
                result.append(r)
        dfs(0, [])
        return result



