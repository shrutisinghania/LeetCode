class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(l, t, i):
            if t == 0:
                res.append(l[:])
                return
            if t < 0:
                return
            for j in range(i, len(candidates)):
                l.append(candidates[j])
                rec(l, t-candidates[j], j)
                l.pop()
        res = []
        rec([], target, 0)
        return res


