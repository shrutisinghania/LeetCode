class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for ind, val in enumerate(nums):
            if val not in d.keys():
                d[val] = [ind]
            else:
                d[val].append(ind)
        c = 0
        for i, v in d.items():
            if len(v) > 1:
                for k in range(len(v)):
                    for m in range(k + 1, len(v)):
                        c += 1
        return c
            