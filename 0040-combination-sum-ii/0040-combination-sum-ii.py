class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(i, t, l):
            if t == 0:
                res.append(l[:])
                return
            if t < 0 or i >= n:
                return
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > t:
                    break
                l.append(candidates[j])
                rec(j+1, t - candidates[j], l)
                l.pop()

        res = []
        candidates.sort()
        n = len(candidates)
        rec(0, target, [])
        return res