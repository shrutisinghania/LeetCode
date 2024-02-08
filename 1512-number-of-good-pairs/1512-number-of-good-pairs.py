class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for ind, val in enumerate(nums):
            if val not in d.keys():
                d[val] = 1
            else:
                d[val] += 1
        c = 0
        for i, v in d.items():
            if v > 1:
                c += (v * (v - 1)) // 2
        return c
            