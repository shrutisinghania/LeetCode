class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = 1
        s = 1
        m = nums[0]
        num = len(nums)
        for n in range(num):
            p *= nums[n]
            s *= nums[num - n - 1]
            m = max(p,s, m)
            if p == 0:
                p = 1
            if s == 0:
                s = 1
        return m
