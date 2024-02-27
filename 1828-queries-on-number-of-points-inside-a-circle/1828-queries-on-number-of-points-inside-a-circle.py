class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        for i, q in enumerate(queries):
            a = 0
            for p in points:
                if (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2 <= q[2] ** 2:
                    a += 1
            queries[i] = a
        return queries
            