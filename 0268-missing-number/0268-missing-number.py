class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = set(nums)
        n = max(nums)+1
        for i in range(n):
            if i not in num:
                return i
        return n