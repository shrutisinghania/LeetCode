class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        n = len(nums)
        l = [1] * n
        for i in range(n):
            l[i] *= prefix
            l[n - 1 - i] *= suffix
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
        return l

