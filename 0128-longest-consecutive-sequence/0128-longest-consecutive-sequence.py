class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        d = 0
        for i in num:
            if i-1 not in num:
                c = 0
                while i in num:
                    i += 1
                    c += 1
                d = max(d, c)
        return d
