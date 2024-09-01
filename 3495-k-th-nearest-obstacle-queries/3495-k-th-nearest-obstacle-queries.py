class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        l = []
        res = []
        for i, j in queries:
            d = abs(i) + abs(j)
            heapq.heappush(l,-d)
            if len(l) > k:
                heapq.heappop(l)
            if len(l) == k:
                res.append(-l[0])
            else:
                res.append(-1)
        return res
