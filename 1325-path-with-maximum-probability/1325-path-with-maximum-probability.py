class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        ans = [0 for _ in range(n)]
        g = [[] for _ in range(n)]
        for index, i in enumerate(edges):
            g[i[0]].append((i[1], succProb[index]))
            g[i[1]].append((i[0], succProb[index]))

        q = []
        heapq.heappush(q, (-1, start_node))
        while q:
            d, n = heapq.heappop(q)
            if ans[n] != 0:
                continue
            if n == end_node:
                return -d
            ans[n] = -d
            for node, dist in g[n]:
                if ans[node] == 0:
                    heapq.heappush(q, (dist * d, node))
        return 0
