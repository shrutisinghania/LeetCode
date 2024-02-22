class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l = [0] * n
        for p in trust:
            l[p[0] - 1] -= 1
            l[p[1] - 1] += 1
        for i, v in enumerate(l):
            if v == n - 1:
                return i+1
        return -1
            