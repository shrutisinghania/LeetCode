class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        s = sum(nums)
        while len(nums) > 2:
            m = max(nums)
            if s - m > m:
                return s
            s -= m
            nums.remove(m)
        return -1