class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        for ind, i in enumerate(nums):
            r -= i
            if l == r:
                return ind
            l += i

        return -1