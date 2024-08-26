class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        m = nums[0]
        for i in nums:
            if total < 0:
                total = 0
            total += i
            m = max(total, m)
        return m
