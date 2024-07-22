class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i >= 1 and nums[i] <= nums[i-1]:
            i -= 1
        if i <= 0:
            return nums.reverse()
        j = len(nums) - 1
        while nums[j] <= nums[i-1]:
            j -= 1
        t = nums[j]
        nums[j] = nums[i-1]
        nums[i-1] = t
        nums[i:] =  nums[i:][::-1]